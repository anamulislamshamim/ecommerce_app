# Generated by Django 4.2.6 on 2023-10-30 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conversationmessage',
            name='conversation',
        ),
        migrations.RemoveField(
            model_name='conversationmessage',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Conversation',
        ),
        migrations.DeleteModel(
            name='ConversationMessage',
        ),
    ]