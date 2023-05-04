import uuid
from azure.storage.queue import QueueClient
Processing_queue_name = "processing-queue"
Connect_str = "DefaultEndpointsProtocol=https;AccountName=storageacc12demo;EndpointSuffix=core.windows.net"
from azure.identity import ClientSecretCredential
tenant_id = ""
Client_id = ""
Client_secret =""
App_credentials = ClientSecretCredential(tenant_id, Client_id, Client_secret)
queue_client =QueueClient.from_connection_string(Connect_str, Processing_queue_name, credential=App_credentials)
print("Client connected to queue")
print("\nLet's PEEK at  the messages in the queue...")
peeked_messages = queue_client.peek_messages(max_messages=15)
for peeked_messages in peeked_messages:
    print("Message: " + peeked_messages.content)