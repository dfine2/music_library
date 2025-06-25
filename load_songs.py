import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project.settings")
django.setup()

from backend.models import Song

songs = [
    Song(
        title="I've Been",
        character="Dan",
        composer="Tom Kitt",
        lyricist="Brian Yorkey",
        show="Next To Normal",
        genre="Musical Theater",
        year=2008,
    ),
    Song(
        title="A Light in the Dark",
        character="Dan",
        composer="Tom Kitt",
        lyricist="Brian Yorkey",
        show="Next To Normal",
        genre="Musical Theater",
        year=2008,
    ),
    Song(
        title="And They're Off",
        character="Gordon",
        composer="William Finn",
        lyricist="William Finn",
        show="A New Brain",
        genre="Musical Theater",
        year=1998
    ),
    Song(
        title="Breeze Off the River",
        character="Jerry",
        composer="David Yazbek",
        lyricist="David Yazbek",
        show="The Full Monty",
        genre="Musical Theater",
        year=2000
    ),
    Song(
        title="C'est Moi",
        character="Lancelot",
        composer="Frederick Loewe",
        lyricist="Alan Jay Lerner",
        show="Camelot",
        genre="Musical Theater",
        year=1960
    ),
    Song(
        title="Evening Star",
        character="Starbuck",
        composer="Henry Schmidt",
        lyricist="Tom Jones",
        show="101 in the Shade",
        genre="Musical Theater",
        year=1967

    ),
    Song(
        title="Falcon in the Dive",
        character="Chauvelin",
        composer="Frank Wildhorn",
        lyricist="Nan Knighton",
        show="The Scarlet Pimpernel",
        genre="Musical Theater",
        year=1997
    ),
    Song(
        title="Fallin'",
        character="Vernon",
        composer="Marvin Hamlisch",
        lyricist="Carole Bayer Sager",
        show="They're Playing Our Song",
        genre="Musical Theater",
        year=1978
    ),
    Song(
        title="Fight the Dragons",
        character="Edward",
        composer="Andrew Lippa",
        lyricist="Andrew Lippa",
        show="Big Fish",
        genre="Musical Theater",
        year=2013
    ),
    Song(
        title="High Flying, Adored",
        character="Che",
        composer="Andrew Lloyd Webber",
        lyricist="Andrew Lloyd Webber",
        show="Evita",
        genre="Musical Theater",
        year=1979
    ),
    Song(
        title="How Can I Call This Home?",
        character="Leo",
        composer="Jason Robert Brown",
        lyricist="Jason Robert Brown",
        show="Parade",
        genre="Musical Theater",
        year=1998
    ),
    Song(
        title="I Am Adolpho",
        character="Adolpho",
        composer="Lisa Lambert and Greg Morrison",
        lyricist="Lisa Lambert and Greg Morrison",
        show="The Drowsy Chaperone",
        genre="Musical Theater",
        year=1998
    ),
    Song(
        title="I Thought That I Could Live",
        character="Death",
        composer="Maury Yeston",
        lyricist="Maury Yeston",
        show="Death Takes a Holiday",
        genre="Musical Theater",
        year=2011
    ),
    Song(
        title="I Wanna Be A Producer",
        character="Leo",
        composer="Mel Brooks",
        lyricist="Mel Brooks",
        show="The Producers",
        genre="Musical Theater",
        year=2001
    ),
    Song(
        title="I'd Rather Be Sailing",
        character="Roger",
        composer="William Finn",
        lyricist="William Finn",
        show="A New Brain",
        genre="Musical Theater",
        year=1998,
    ),
    Song(
        title="If the World Turned Upside Down",
        character="Barry",
        composer="Gary Barlow and Eliot Kennedy",
        lyricist="Gary Barlow and Eliot Kennedy",
        show="Finding Neverland",
        genre="Musical Theater",
        year=2014
    ),
    Song(
        title="I'm Alive",
        character="Gabe",
        composer="Tom Kitt",
        lyricist="Brian Yorkey",
        show="Next To Normal",
        genre="Musical Theater",
        year=2008
    ),
    Song(
        title="I'm Allergic to Cats",
        character="",
        composer="Neil Bartram",
        lyricist="Neil Bartram",
        show="The Theory of Relativity",
        genre="Musical Theater",
        year=2015
    ),
    Song(
        title="It's Hard to Speak My Heart",
        character="Leo",
        composer="Jason Robert Brown",
        lyricist="Jason Robert Brown",
        show="Parade",
        genre="Musical Theater",
        year=1998
    ),
    Song(
        title="Marry Me a Little",
        character="Bobby",
        composer="Stephen Sondheim",
        lyricist="Stephen Sondheim",
        show="Company",
        genre="Musical Theater",
        year=1970
    ),
    Song(
        title="My Friends",
        character="Sweeney",
        composer="Stephen Sondheim",
        lyricist="Stephen Sondheim",
        show="Sweeney Todd",
        genre="Musical Theater",
        year=1979
    ),
    Song(
        title="Nothing More",
        character="",
        composer="Tim Rosser and Charlie Sohne",
        lyricist="Tim Rosser and Charlie Sohne",
        show="With the Right Music",
        genre="Musical Theater",
        year=2014
    ),
    Song(
        title="Now",
        character="Fredrik",
        composer="Stephen Sondheim",
        lyricist="Stephen Sondheim",
        show="A Little Night Music",
        genre="Musical Theater",
        year=1973
    ),
    Song(
        title="Old Devil Moon",
        character="Woody",
        composer="Burton Lane",
        lyricist="E.Y. Harburg",
        show="Finian's Rainbow",
        genre="Musical Theater",
        year=1947

    ),
    Song(
        title="To Each His Dulcinea",
        character="Padre",
        composer="Mitch Leigh",
        lyricist="Joe Darion",
        show="Man of La Mancha",
        genre="Musical Theater",
        year=1965
    ),
    Song(
        title="Wicked Little Town",
        character="Hedwig",
        composer="Stephen Trask",
        lyricist="Stephen Trask",
        show="Hedwig and the Angry Inch",
        genre="Musical Theater",
        year=1998
    ),
    Song(
        title="Winter's On the Wing",
        character="Dickon",
        composer="Lucy Simon",
        lyricist="Marsha Norman",
        show="The Secret Garden",
        genre="Musical Theater",
        year=1991
    ),
    Song(
        title="As It Was",
        artist="Harry Styles",
        album="Harry's House",
        genre="Pop",
        year=2022
    ),
    Song(
        title="Falling",
        artist="Harry Styles",
        album="Fine Line",
        genre="Pop",
        year=2019
    ),
    Song(
        title="Flightless Bird, American Mouth",
        artist="Iron & Wine",
        album="The Shepherd's Dog",
        genre="Pop",
        year=2007
    ),
    Song(
        title="Love Yourself",
        artist="Justin Bieber",
        album="Purpose",
        genre="Pop",
        year=2015
    ),
    Song(
        title="Over My Head (Cable Car)",
        artist="The Fray",
        album="Stealth",
        genre="Pop",
        year=2005
    ),
    Song(
        title="Say You Won't Let Go",
        artist="James Arthur",
        album="Back From the Edge",
        genre="Pop",
        year=2016
    ),
]

for song in songs:
    song.save()
