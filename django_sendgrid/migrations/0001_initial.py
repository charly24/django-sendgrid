class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Argument',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('key', models.CharField(max_length=255)),
                ('data_type', models.IntegerField(choices=[(0, 'Unknown'), (1, 'Boolean'), (2, 'Integer'), (3, 'Float'), (4, 'Complex'), (5, 'String')], default=0, verbose_name='Data Type')),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Arguments',
                'verbose_name': 'Argument',
            },
        ),
        migrations.CreateModel(
            name='BounceReason',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('reason', models.TextField()),
            ],
            options={'verbose_name': 'Bounce Reason', 'verbose_name_plural': 'Bounce Reasons'},
        ),
        migrations.CreateModel(
            name='BounceType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('type', models.CharField(unique=True, max_length=32)),
            ],
            options={'verbose_name': 'Bounce Type', 'verbose_name_plural': 'Bounce Types'},
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=150)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='ClickUrl',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('url', models.TextField()),
            ],
            options={'verbose_name': 'Click Url', 'verbose_name_plural': 'Click Urls'},
        ),
        migrations.CreateModel(
            name='EmailMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('message_id', models.CharField(blank=True, unique=True, null=True, max_length=36, editable=False, help_text='UUID')),
                ('from_email', models.CharField(help_text="Sender's e-mail", max_length=254)),
                ('to_email', models.CharField(help_text="Primiary recipient's e-mail", max_length=254)),
                ('category', models.CharField(blank=True, help_text='Primary SendGrid category', null=True, max_length=150)),
                ('response', models.IntegerField(blank=True, help_text='Response received from SendGrid after sending', null=True)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Email Messages',
                'verbose_name': 'Email Message',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Events',
                'verbose_name': 'Event',
            },
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(unique=True, max_length=128)),
            ],
            options={'verbose_name': 'Event Type', 'verbose_name_plural': 'Event Types'},
        ),
        migrations.CreateModel(
            name='UniqueArgument',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('data', models.CharField(max_length=255)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified_time', models.DateTimeField(auto_now=True)),
                ('argument', models.ForeignKey(on_delete=models.CASCADE, to='django_sendgrid.Argument')),
            ],
            options={
                'verbose_name_plural': 'Unique Arguments',
                'verbose_name': 'Unique Argument',
            },
        ),
        migrations.CreateModel(
            name='BounceEvent',
            fields=[
                ('event_ptr', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, auto_created=True, to='django_sendgrid.Event', parent_link=True, serialize=False)),
                ('status', models.CharField(max_length=16)),
                ('bounce_reason', models.ForeignKey(on_delete=models.CASCADE, to='django_sendgrid.BounceReason', null=True)),
                ('bounce_type', models.ForeignKey(on_delete=models.CASCADE, to='django_sendgrid.BounceType', null=True)),
            ],
            options={
                'verbose_name_plural': 'Bounce Events',
                'verbose_name': 'Bounce Event',
            },
            bases=('django_sendgrid.event',),
        ),
        migrations.CreateModel(
            name='ClickEvent',
            fields=[
                ('event_ptr', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, auto_created=True, to='django_sendgrid.Event', parent_link=True, serialize=False)),
                ('click_url', models.ForeignKey(on_delete=models.CASCADE, to='django_sendgrid.ClickUrl')),
            ],
            options={
                'verbose_name_plural': 'Click Events',
                'verbose_name': 'Click Event',
            },
            bases=('django_sendgrid.event',),
        ),
        migrations.CreateModel(
            name='DeferredEvent',
            fields=[
                ('event_ptr', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, auto_created=True, to='django_sendgrid.Event', parent_link=True, serialize=False)),
                ('response', models.TextField()),
                ('attempt', models.IntegerField()),
            ],
            bases=('django_sendgrid.event',),
            options={'verbose_name': 'Deferred Event', 'verbose_name_plural': 'Deferred Events'},
        ),
        migrations.CreateModel(
            name='DeliverredEvent',
            fields=[
                ('event_ptr', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, auto_created=True, to='django_sendgrid.Event', parent_link=True, serialize=False)),
                ('response', models.TextField()),
            ],
            bases=('django_sendgrid.event',),
            options={'verbose_name': 'Deliverred Event', 'verbose_name_plural': 'Deliverred Events'},
        ),
        migrations.CreateModel(
            name='DroppedEvent',
            fields=[
                ('event_ptr', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, auto_created=True, to='django_sendgrid.Event', parent_link=True, serialize=False)),
                ('reason', models.CharField(max_length=255)),
            ],
            bases=('django_sendgrid.event',),
            options={'verbose_name': 'Dropped Event', 'verbose_name_plural': 'Dropped Events'},
        ),
        migrations.CreateModel(
            name='EmailMessageAttachmentsData',
            fields=[
                ('email_message', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, to='django_sendgrid.EmailMessage', related_name='attachments', serialize=False)),
                ('data', models.TextField(editable=False, verbose_name='Attachments')),
            ],
            options={
                'verbose_name_plural': 'Email Message Attachments Data',
                'verbose_name': 'Email Message Attachment Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageBccData',
            fields=[
                ('email_message', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, to='django_sendgrid.EmailMessage', related_name='bcc', serialize=False)),
                ('data', models.TextField(editable=False, verbose_name='Blind Carbon Copies')),
            ],
            options={
                'verbose_name_plural': 'Email Message Bcc Data',
                'verbose_name': 'Email Message Bcc Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageBodyData',
            fields=[
                ('email_message', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, to='django_sendgrid.EmailMessage', related_name='body', serialize=False)),
                ('data', models.TextField(editable=False, verbose_name='Body')),
            ],
            options={
                'verbose_name_plural': 'Email Message Body Data',
                'verbose_name': 'Email Message Body Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageCcData',
            fields=[
                ('email_message', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, to='django_sendgrid.EmailMessage', related_name='cc', serialize=False)),
                ('data', models.TextField(editable=False, verbose_name='Carbon Copies')),
            ],
            options={
                'verbose_name_plural': 'Email Message Cc Data',
                'verbose_name': 'Email Message Cc Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageExtraHeadersData',
            fields=[
                ('email_message', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, to='django_sendgrid.EmailMessage', related_name='extra_headers', serialize=False)),
                ('data', models.TextField(editable=False, verbose_name='Extra Headers')),
            ],
            options={
                'verbose_name_plural': 'Email Message Extra Headers Data',
                'verbose_name': 'Email Message Extra Headers Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageSendGridHeadersData',
            fields=[
                ('email_message', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, to='django_sendgrid.EmailMessage', related_name='sendgrid_headers', serialize=False)),
                ('data', models.TextField(editable=False, verbose_name='SendGrid Headers')),
            ],
            options={
                'verbose_name_plural': 'Email Message SendGrid Headers Data',
                'verbose_name': 'Email Message SendGrid Headers Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageSubjectData',
            fields=[
                ('email_message', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, to='django_sendgrid.EmailMessage', related_name='subject', serialize=False)),
                ('data', models.TextField(editable=False, verbose_name='Subject')),
            ],
            options={
                'verbose_name_plural': 'Email Message Subject Data',
                'verbose_name': 'Email Message Subject Data',
            },
        ),
        migrations.CreateModel(
            name='EmailMessageToData',
            fields=[
                ('email_message', models.OneToOneField(on_delete=models.CASCADE, primary_key=True, to='django_sendgrid.EmailMessage', related_name='to', serialize=False)),
                ('data', models.TextField(editable=False, verbose_name='To')),
            ],
            options={
                'verbose_name_plural': 'Email Message To Data',
                'verbose_name': 'Email Message To Data',
            },
        ),
        migrations.AddField(
            model_name='uniqueargument',
            name='email_message',
            field=models.ForeignKey(on_delete=models.CASCADE, to='django_sendgrid.EmailMessage'),
        ),
        migrations.AddField(
            model_name='event',
            name='email_message',
            field=models.ForeignKey(on_delete=models.CASCADE, to='django_sendgrid.EmailMessage'),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=models.CASCADE, to='django_sendgrid.EventType'),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='arguments',
            field=models.ManyToManyField(to='django_sendgrid.Argument', through='django_sendgrid.UniqueArgument'),
        ),
        migrations.AddField(
            model_name='emailmessage',
            name='categories',
            field=models.ManyToManyField(to='django_sendgrid.Category'),
        ),
        migrations.RunPython(load_fixture),
    ]
