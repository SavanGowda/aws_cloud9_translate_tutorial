import boto3
import click

@click.command()
@click.option('--phrase', prompt='Put in a phrase in any language to translate',
    help='A tool to translate texts')
def action(phrase):

    client = boto3.client('translate', region_name = "us-west-2")
    # text = "Hola mi nombre es Savan"
    click.echo(click.style(f"Translate the phrase: {phrase}", fg='red'))
    result = client.translate_text(Text=phrase, SourceLanguageCode="auto",
        TargetLanguageCode="de")
        
    text = result["TranslatedText"]
    
    click.echo(click.style(f"Translated phrase: {text}", bg='green', fg='white'))
    
    
if __name__ == '__main__':
    action()
