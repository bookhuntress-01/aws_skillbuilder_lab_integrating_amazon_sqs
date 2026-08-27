# update_status.py

import time
import sys
import boto3


sqs = boto3.client("sqs")

print("=" * 60)
print("Background Check Status Update Script")
print("=" * 60)

# Set status to not started
print("\n[1/3] Sending status: NOT STARTED")
print("Message: The Background Check Job has not been started. Currently gathering required data to process.")
response = sqs.send_message(
    QueueUrl='BackgroundCheckApp',
    MessageBody='The Background Check Job has not been started. Currently gathering required data to process.'
)
print(f"✓ Message sent successfully! MessageId: {response['MessageId']}")
print("Waiting 8 seconds before next update...")
# Timeout simulates various processes running in-between automatic status updates
time.sleep(8)


# Set status to started
print("\n[2/3] Sending status: STARTED")
print("Message: The Background Check Job has been started.")
response = sqs.send_message(
    QueueUrl='BackgroundCheckApp',
    MessageBody='The Background Check Job has been started.'
)
print(f"✓ Message sent successfully! MessageId: {response['MessageId']}")
print("Waiting 8 seconds before next update...")
# Timeout simulates various processes running in-between automatic status updates
time.sleep(8)

# Set status to finished
print("\n[3/3] Sending status: FINISHED")
print("Message: The Background Check Job has finished.")
response = sqs.send_message(
    QueueUrl='BackgroundCheckApp',
    MessageBody='The Background Check Job has finished.'
)
print(f"✓ Message sent successfully! MessageId: {response['MessageId']}")

print("\n" + "=" * 60)
print("All status updates sent successfully!")
print("=" * 60)
