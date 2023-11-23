class JournalingFileSystem:
    def __init__(self):
        self.files = {}  # Simulating the file system
        self.journal = []  # Journal to log operations

    def write_to_journal(self, action, file_name, content=None):
        """Log the operation to the journal."""
        self.journal.append((action, file_name, content))

    def commit_journal(self):
        """Apply the changes in the journal to the file system."""
        for action, file_name, content in self.journal:
            if action == "create":
                self.files[file_name] = content
            elif action == "delete":
                del self.files[file_name]
            elif action == "update":
                self.files[file_name] = content

        # Clear the journal after committing
        self.journal.clear()

    def create_file(self, file_name, content):
        """Create a file in the journal."""
        self.write_to_journal("create", file_name, content)

    def delete_file(self, file_name):
        """Delete a file in the journal."""
        self.write_to_journal("delete", file_name)

    def update_file(self, file_name, new_content):
        """Update a file in the journal."""
        self.write_to_journal("update", file_name, new_content)

    def view_file_system(self):
        """View the current state of the file system."""
        print("File System State:")
        if self.files:
            for file, content in self.files.items():
                print(f"  File: {file}, Content: '{content}'")
        else:
            print("  No files in the system.")

        print("\nJournal Entries:")
        if self.journal:
            for action, file, content in self.journal:
                entry = f"  Action: {action}, File: {file}"
                entry += f", Content: '{content}'" if content else ""
                print(entry)
        else:
            print("  No pending journal entries.")


    def view_file_system(self):
        """View the current state of the file system."""
        print("File System State:")
        if self.files:
            for file, content in self.files.items():
                print(f"  File: {file}, Content: '{content}'")
        else:
            print("  No files in the system.")

        print("\nJournal Entries:")
        if self.journal:
            for action, file, content in self.journal:
                entry = f"  Action: {action}, File: {file}"
                entry += f", Content: '{content}'" if content else ""
                print(entry)
        else:
            print("  No pending journal entries.")



fs = JournalingFileSystem()

# Create some files
fs.create_file("file1.txt", "Hello, world!")
fs.create_file("file2.txt", "This is a test.")
fs.view_file_system()

# Commit the changes
fs.commit_journal()
fs.view_file_system()

# Update a file
fs.update_file("file1.txt", "Hello, Python!")
fs.view_file_system()

# Delete a file
fs.delete_file("file2.txt")
fs.view_file_system()

# Commit the changes
fs.commit_journal()
fs.view_file_system()
