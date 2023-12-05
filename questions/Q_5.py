# Q 5) What is a QuerySet?Write program to create a new Post object in database:

# A QuerySet in Django is a representation of a set of database queries. It allows you to retrieve, filter, and manipulate data from the database. Here's an example program to create a new Post object in the database:

from myapp.models import Post

# Create a new Post object
new_post = Post.objects.create(
    title='My First Post',
    content='This is the content of my first post.',
    author='John Doe'
)

# Save the object to the database
new_post.save()
