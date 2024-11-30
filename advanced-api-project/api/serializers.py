from rest_framework import serializers

from api.models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for converting Book instances to JSON and vice versa.

    This serializer takes information about books from the database and serializes it
    into JSON format for use in API responses. It is also responsible for deserializing
    data when creating or updating Book instances.

    Attributes:
        model (Book): The model that this serializer is tied to.
        fields (list[str]): A list of fields from the Book model to include in the serialized output.
    """
    # author_name = serializers.CharField(source='author.name', read_only=True)
    class Meta:
        """
        Meta options for the Book serializer.

        Attributes:
            model (Book): The model that this serializer will operate on.
            fields (str or list): The fields to include in the serialized output, in this case, all fields from the model.
        """
        model = Book
        fields = '__all__'
        # fields = ['id', 'title','author','author_name']# This includes all fields of the Book model in the serialization

    def validate(self, attrs):
        """
        Validate the 'publication_year' field to ensure it is not in the future.
    
        This method checks the 'publication_year' attribute from the provided data
        (typically from the request) to ensure that the publication year is not later 
        than the current year. If the publication year is in the future, a validation 
        error is raised.
    
        Args:
            attrs (dict): A dictionary of validated attributes for the instance, 
                          typically the fields from the serializer's data.
    
        Returns:
            dict: The validated attributes, which can be modified if necessary 
                  (in this case, no modification is made).
    
        Raises:
            serializers.ValidationError: If the 'publication_year' is greater 
                                          than the current year, an error is raised.
        """
        from datetime import datetime
        current_year = datetime.now().year
        publication_year = attrs['publication_year']
        if publication_year > current_year:
            raise serializers.ValidationError("'Publication Year' cannot be in the future")
        elif publication_year < 0:
            raise serializers.ValidationError("'Publication Year' cannot be negative")
        return attrs

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for converting Author instances to JSON with related Books data.

    This serializer provides a detailed representation of an Author, including a nested 
    list of the author's books (if any). It is designed for use in API views to return 
    information about authors and their works.

    Attributes:
        books (BookSerializer): A nested serializer that represents the books written by the author.
    """

    books = BookSerializer(many=True, read_only=True)  # Nested serializer for the books of the author

    class Meta:
        """
        Meta options for the Author serializer.

        Attributes:
            model (Author): The model that this serializer will operate on.
            fields (list[str]): The fields to include in the serialized output, which includes the author's name and their books.
        """
        model = Author
        fields = ['name', 'books']  # Include the author's name and their books in the serialized output

