my_file = open('hp_timeline.html', 'w')
my_file.write('<html><head><title>Hogwarts Students Timeline</title>
        <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js"></script>
        <!-- BEGIN TimelineJS -->
        <script type="text/javascript" src="http://cdn.knightlab.com/libs/timeline/latest/js/storyjs-embed.js"></script>')
my_file.write('</head><body>Hello world</body></html>')
print(my_file)
    
