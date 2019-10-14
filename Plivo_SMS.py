import plivo

client = plivo.RestClient()
message = client.messages.create(
    src='+12192173175',
    dst='+18328535174',
    text='This is a test'
)