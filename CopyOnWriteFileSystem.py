class CoWFileSystem:
    def __init__(self):
        self.file_system = {}
        self.journal = []

    def create_file(self, path, content):
        self.file_system[path] = content

    def read_file(self, path):
        return self.file_system.get(path, None)

    def update_file(self, path, new_content):
        # Copy-On-Write: Write to a new location first
        temp_path = path + "_temp"
        self.file_system[temp_path] = new_content

        # Journal the update
        self.journal.append((path, temp_path))

    def commit_changes(self):
        # Update the main file system structure after successful writes
        for original_path, temp_path in self.journal:
            self.file_system[original_path] = self.file_system.pop(temp_path)

        # Clear the journal
        self.journal.clear()

    def view_file_system(self):
        return self.file_system

# Initialize the file system
fs = CoWFileSystem()

# Create a file
fs.create_file("/mydoc.txt", "Initial content")

# File System State: {'/mydoc.txt': 'Initial content'}
print("File System State:", fs.view_file_system())

# Update the file
fs.update_file("/mydoc.txt", "Updated content")

# File System State: {'/mydoc.txt': 'Initial content', '/mydoc.txt_temp': 'Updated content'}
print("File System State:", fs.view_file_system())

# Commit the changes
fs.commit_changes()

# File System State: {'/mydoc.txt': 'Updated content'}
print("File System State:", fs.view_file_system())

# Read the file
print("Content of /mydoc.txt:", fs.read_file("/mydoc.txt"))

# File System State: {'/mydoc.txt': 'Updated content'}
print("File System State:", fs.view_file_system())
