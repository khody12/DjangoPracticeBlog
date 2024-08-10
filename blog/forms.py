from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(label="Leave a comment!",max_length=300,error_messages={
        "required":"Your comment can't be empty",
        "max_length":"Your comment is too long"
    })