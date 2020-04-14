import boto3

client = boto3.client('translate', region_name = "us-west-2")

text = "Hola mi nombre es Savan"

result = client.translate_text(Text=text, SourceLanguageCode="auto",
    TargetLanguageCode="en")
    
print(result["TranslatedText"])