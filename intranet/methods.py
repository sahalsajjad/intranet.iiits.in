
def file_folder_allocator(instance, filename):
	return str('/'.join([ instance.user.username, filename])) 
