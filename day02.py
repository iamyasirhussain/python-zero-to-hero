current_replicas = "3"
scale_up_by = "2"
new_count = int(current_replicas) + int(scale_up_by)
print(f"Scaling from {current_replicas} replicas to {new_count}")