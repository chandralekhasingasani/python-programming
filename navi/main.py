import docker
import csv

class MyKafka:

    def __init__(self,container_id):
        self.client = docker.from_env()
        self.container = self.client.containers.get(container_id)
        self.topics = []
        self.partition = []
        self.replication_factor = []
        self.current_kafka_topics = []

    def get_current_topics(self):
        filename = open('datakafka.csv', 'r')
        file = csv.DictReader(filename)
        for col in file:
            self.topics.append(col['TOPICS'])
            self.partition.append(col['PARTITIONS'])
            self.replication_factor.append(col['REPLICATION_FACTOR'])
        result = self.container.exec_run('/opt/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper:2181')
        self.current_kafka_topics = result.output.decode().splitlines()

    def create_topic(self):
        count=0
        for i in self.topics:
            if i not in self.current_kafka_topics:
                result = self.container.exec_run(
                    "/opt/kafka/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor {0} --partitions {1} --topic {2}".format(
                        self.replication_factor[count], self.partition[count], self.topics[count]))
                if result.exit_code == 0:
                    print('Topic named ', self.topics[count], ' has been created')
                else:
                    print('Topic name ', self.topics[count], ' could not be  created',result.output.decode())
            count+=1

    def delete_topic(self):
        count=0
        self.get_current_topics()
        for i in self.current_kafka_topics:
            if i not in self.topics:
                result = self.container.exec_run(
                    "/opt/kafka/bin/kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic {0}".format(i))
                if result.exit_code == 0:
                    print('Topic named ', i, ' has been deleted')
            count+=1


kafka_client = MyKafka('789cc1639018')
kafka_client.get_current_topics()
kafka_client.create_topic()
kafka_client.delete_topic()