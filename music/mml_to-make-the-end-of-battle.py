import pyxel

class PreludeMusic:
    def __init__(self, p, m):
        self.done = False
        self.prelude = p
        self.melody = m
    
    def playing(self):
        if pyxel.play_pos(0) is None and not self.done:
            pyxel.playm(self.prelude, loop=False)
            self.done = True
        if pyxel.play_pos(0) is None and self.done:
            pyxel.playm(self.melody, loop=False)

EXTENDED_CHANNELS = [
    (0.1, 0),  # Lead Melody
    (0.08, 20),  # Detuned Lead Melody
    (0.05, 0),  # Chord Backing 1
    (0.05, 5),  # Chord Backing 2
    (0.05, 5),  # Chord Backing 3
    (0.12, 0),  # Bass Line
    (0.08, 20),  # Drums1
    (0.08, 0),  # Drums2
]

def extend_audio():
    channels = []
    for gain, detune in EXTENDED_CHANNELS:
        channel = pyxel.Channel()
        channel.gain = gain
        channel.detune = detune
        channels.append(channel)
    pyxel.channels.from_list(channels)

    pyxel.tones[2].waveform.from_list(
        [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
    )
    pyxel.tones[0].waveform.from_list(
        [0,1,2,3,4,5,6,7,8,9,10,10,10,10,10,10,10,10,10,10,10,10,9,8,7,6,5,4,3,2,1,0]
    )

class PreludeMusic:
    def __init__(self, p, m):
        self.done = False
        self.prelude = p
        self.melody = m
    
    def playing(self):
        if pyxel.play_pos(0) is None:
            if  not self.done:
                pyxel.playm(self.prelude, loop=False)
                self.done = True
            else:
                pyxel.playm(self.melody, loop=False)

class App:
    def __init__(self):
        pyxel.init(128, 120, display_scale=2, fps=60)
        extend_audio()
        self.bgm = PreludeMusic(0,1)
            
        envelope = "t110 x0:7777555444333333456 x1:66665454545454543434343232321212121111 x4:5210 x5:310"
        prelude_ch1 = [
            envelope,
            "r1",
        ]
        melody_ch1 = [
            envelope,
            "x0 @2 o2l16 e-ega&a<aaa>c+<a>d<a>e<a>d<a l32o2 agagagag >agagagag l16<<ab->c<b-ab->cd",
            "x0 o3 l16 c+<ab-gafgeb-gafgefd c+defgab->c+ec+<b->fc+<b-<ef g4.ab->c+4.ef gfefgab->c+ l8 eefg",
            "x0 o3 l16 fecd&d2~<a>cdc fecd&d2~<agfe x0 o2 l8 f.d.fg.e.ga.f.de.g.b-a2~ l16 >defgagfe x0 o3 l8 g.e.c<g.>c.e l16 fd<afda>dfec<gecg>ce",
            "x0 o2 l16 dfa>c+dfa>c+d2~",
            "x0 o3 l16 fecd&d2~<a>cdc fecd&d2~<agfe x0 o2 l8 f.d.fg.e.ga.f.de.g.b-a2~ l16 >defgagfe x0 o3 l8 g.e.c<g.>c.e l16 fd<afda>dfec<gecg>ce",
            "x0 o2 l32 e-8.<b->e-g8.e-gb-8.gb->e-4",
            "x0 o2 l16 a4dfga&a8g8fg8>d&d8<a8gf8e&e8f8&fg8. a4dfga&a8g8fg8>d&d8d8e8d8d4c+4",
            "x0 o2 l16 dfadfadfadfae-gb-g dfadfadfadfacceg dfadfadfadfae-gb-g dfadfadfadfacceg",
            "x0 @2 o2l16 e-ega&a<aaa>c+<a>d<a>e<a>d<a l32o2 agagagag >agagagag l16<<ab->c<b-ab->cd",
            "x0 o3 l16 c+<ab-gafgeb-gafgefd c+defgab->c+ec+<b->fc+<b-<ef g4.ab->c+4.ef gfefgab->c+ l8 eefg",
            "x0 o3 l16 fecd&d2~<a>cdc fecd&d2~<agfe x0 o2 l8 f.d.fg.e.ga.f.de.g.b-a2~ l16 >defgagfe x0 o3 l8 g.e.c<g.>c.e l16 fd<afda>dfec<gecg>ce",
            "x0 o2 l16 dfa>c+dfa>c+d2~",
            "x0 o3 l16 fecd&d2~<a>cdc fecd&d2~<agfe x0 o2 l8 f.d.fg.e.ga.f.de.g.b-a2~ l16 >defgagfe x0 o3 l8 g.e.c<g.>c.e l16 fd<afda>dfec<gecg>ce",
            "x0 o2 l32 e-8.<b->e-g8.e-gb-8.gb->e-4",
            "x0 o2 l16 dr8dr8dd&d2",
            "r1r1"
        ]
        
        prelude_ch2 = [
            envelope,
            "r1",
        
        ]
        melody_ch2 = [
            envelope,
            "x0 @2 o2 l16 e-ega&a<aaa>c+<a>d<a>e<a>d<a l32o2 edededed >edededed l16<<ab->c<b-ab->cd",
            "x0 o3 l16 c+<ab-gafgeb-gafgefd c+defgab->c+ec+<b->fc+<b-<ef g4.ab->c+4.ef gfefgab->c+ l8 eefg",
            "x0 o3 l16 fecd&d2~<a>cdc fecd&d2~<agfe x0 o2 l8 f.d.fg.e.ga.f.de.g.b-a2~ l16 >defgagfe x0 o3 l8 g.e.c<g.>c.e l16 fd<afda>dfec<gecg>ce",
            "x0 o2 l16 dfa>c+dfa>c+d2~",
            "x0 o3 l16 fecd&d2~<a>cdc fecd&d2~<agfe x0 o2 l8 f.d.fg.e.ga.f.de.g.b-a2~ l16 >defgagfe x0 o3 l8 g.e.c<g.>c.e l16 fd<afda>dfec<gecg>ce",
            "x0 o2 l32 e-8.<b->e-g8.e-gb-8.gb->e-4",
            "x0 o2 l16 a4dfga&a8g8fg8>d&d8<a8gf8e&e8f8&fg8. a4dfga&a8g8fg8>d&d8d8e8d8d4c+4",
            "x0 o2 l16 dfadfadfadfae-gb-g dfadfadfadfacceg dfadfadfadfae-gb-g dfadfadfadfacceg",
            "x0 @2 o2 l16 e-ega&a<aaa>c+<a>d<a>e<a>d<a l32o2 edededed >edededed l16<<ab->c<b-ab->cd",
            "x0 o3 l16 c+<ab-gafgeb-gafgefd c+defgab->c+ec+<b->fc+<b-<ef g4.ab->c+4.ef gfefgab->c+ l8 eefg",
            "x0 o3 l16 fecd&d2~<a>cdc fecd&d2~<agfe x0 o2 l8 f.d.fg.e.ga.f.de.g.b-a2~ l16 >defgagfe x0 o3 l8 g.e.c<g.>c.e l16 fd<afda>dfec<gecg>ce",
            "x0 o2 l16 dfa>c+dfa>c+d2~",
            "x0 o3 l16 fecd&d2~<a>cdc fecd&d2~<agfe x0 o2 l8 f.d.fg.e.ga.f.de.g.b-a2~ l16 >defgagfe x0 o3 l8 g.e.c<g.>c.e l16 fd<afda>dfec<gecg>ce",
            "x0 o2 l32 e-8.<b->e-g8.e-gb-8.gb->e-4",
            "x0 o2 l16 dr8dr8dd&d2",
            "r1r1"
        ]
        
        prelude_ch3 = [
            envelope,
            "r1"
        ]
        melody_ch3 = [
            envelope,
            "x1 @1 o2 l2 eg l16 >b-gec<b-gec efg+fefga",
            "x1 o2 l2 b->e g4.f8e <b->e g l8 ec+de",
            "x1 o2 l16 b-aga&a4 l8 >agfe< l16 b-aga&a4 l8 >agfe< x1 o3 l8 d.<a.>d e.c.e f.d.<a>c+.e.g <f2 l4 a>d x1 o3 l2 ecge",
            "x1 o3 d2 l8 dc+<b>c+",
            "x1 o2 l16 b-aga&a4 l8 >agfe< l16 b-aga&a4 l8 >agfe< x1 o3 l8 d.<a.>d e.c.e f.d.<a>c+.e.g <f2 l4 a>d x1 o3 l2 ecge",
            "x1 o3 l4 b-. r8r2",
            "x1 o2 l16 ffffrff8ffffrff8 b-b-b-b-rb-b-8aaaaraa8 >ffffrff8ffffrff8 b-b-b-b-rb-b-8aaaaraa8",
            "x1 o2 l16 aa>a<aa>a<aa>a<aa>a<b->e-ge-< aa>a<aa>a<aa>a<aa>aeeg>c o2 aa>a<aa>a<aa>a<aa>a<b->e-ge-< aa>a<aa>a<aa>a<aa>aeeg>c",
            "x1 @1 o2 l2 eg l16 >b-gec<b-gec efg+fefga",
            "x1 o2 l2 b->e g4.f8e <b->e g l8 ec+de",
            "x1 o2 l16 b-aga&a4 l8 >agfe< l16 b-aga&a4 l8 >agfe< x1 o3 l8 d.<a.>d e.c.e f.d.<a>c+.e.g <f2 l4 a>d x1 o3 l2 ecge",
            "x1 o3 d2 l8 dc+<b>c+",
            "x1 o2 l16 b-aga&a4 l8 >agfe< l16 b-aga&a4 l8 >agfe< x1 o3 l8 d.<a.>d e.c.e f.d.<a>c+.e.g <f2 l4 a>d x1 o3 l2 ecge",
            "x1 o3 l4 b-. r8r2",
            "x1 o2 l16 ar8ar8aa&a8r4.",
            "r1r1"
        ]
        
        prelude_ch4 = [
            envelope,
            "r1",
        ]
        melody_ch4 = [
            envelope,
            "x1 @1 o2 l2 ce l16 gec<b-gec<b- cdedcdef",
            "x1 o2 l2 gb- e4.d8c+ <gb- >e l8 c+<ab>c+",
            "x1 o2 l16 agdf&f4 l8 >fedc< l16 agdf&f4 l8 >fedc< x1 o2 l8 a.f.a>c.<g.>c d.<a.fg.>c+.e<d2 l4 fa x1 o2 l2 c<g>ec",
            "x1 o1 a2 l8 aaba",
            "x1 o2 l16 agdf&f4 l8 >fedc< l16 agdf&f4 l8 >fedc< x1 o2 l8 a.f.a>c.<g.>c d.<a.fg.>c+.e<d2 l4 fa x1 o2 l2 c<g>ec",
            "x1 o3 l4 g. r8r2",
            "x1 o3 l16 eeeeree8ccccecc8 ffffrff8eeeeree8 >ddddrdd8ccccrcc8 ffffrff8eeeeree8",
            "x1 o2 l16 fd>d<fd>d<df>d<df>d<gb->e<b- fd>d<fd>d<df>d<df>d<gg>ce o2 fd>d<fd>d<df>d<df>d<gb->e<b- fd>d<fd>d<df>d<df>d<gg>ce",
            "x1 @1 o2 l2 ce l16 gec<b-gec<b- cdedcdef",
            "x1 o2 l2 gb- e4.d8c+ <gb- >e l8 c+<ab>c+",
            "x1 o2 l16 agdf&f4 l8 >fedc< l16 agdf&f4 l8 >fedc< x1 o2 l8 a.f.a>c.<g.>c d.<a.fg.>c+.e<d2 l4 fa x1 o2 l2 c<g>ec",
            "x1 o1 a2 l8 aaba",
            "x1 o2 l16 agdf&f4 l8 >fedc< l16 agdf&f4 l8 >fedc< x1 o2 l8 a.f.a>c.<g.>c d.<a.fg.>c+.e<d2 l4 fa x1 o2 l2 c<g>ec",
            "x1 o3 l4 g. r8r2",
            "x1 o2 l16 fr8fr8ff&f8r4.",
            "r1r1"
        ]
        
        prelude_ch5 = [
            envelope,
            "r1",
        ]
        melody_ch5 = [
            envelope,
            "x1 @1 r1 o2l16 ec+<b-gec+<b-g r2",
            "x1 o2 l2 eg b-4.a8g ea b- r2",
            "l1 rrrrrrr",
            "r1",
            "l1 rrrrrrr",
            "r1",
            "r1r1r1r1",
            "r1r1r1r1",
            "r1r1r1r1",
            "x1 @1 r1 o2l16 ec+<b-gec+<b-g r2",
            "x1 o2 l2 eg b-4.a8g ea b- r2",
            "l1 rrrrrrr",
            "r1",
            "l1 rrrrrrr",
            "r1",
            "r1r1r1r1",
            "x1 o2 l16 dr8dr8dd&d8r4.",
            "r1r1"
        ]
        
        prelude_ch6 = [
            envelope,
            "r1",
        ]
        melody_ch6 = [
            envelope,
            "@0 q5 v7 o0l16 aaaa>c+<a>d<a>e<a>f<a>g<a>f<a >e<a>f<a>e<a>d<a>c+<abgab>c<b",
            "o0 l16 aaarr8>a8a<aaraa>c+d< aaarr8>a8a<aaraa>c+d< aaarr8>a8a<aaraa>c+d< aaarr8>a8<aa>a<ab-b->c+c+",
            "o1 l16 dddddddddddddddd cccccccccccccccc o0 l16 b-b->fb->d<b-fb-ccg>cec<g>c <ddfa>d<afd<a>age<aaaa> dddddddddddddddd o1 l16 cccccccccccccccc <b-b->fb->d<b-fb- ccg>cec<g>c",
            "o1 l16 ddfa>d<afd <a>age<aaaa",
            "o1 l16 dddddddddddddddd cccccccccccccccc o0 l16 b-b->fb->d<b-fb-ccg>cec<g>c <ddfa>d<afd<a>age<aaaa> dddddddddddddddd o1 l16 cccccccccccccccc <b-b->fb->d<b-fb- ccg>cec<g>c",
            "o1 l16 e-e-b-e-ge-ae- b-e->e-<e->g<e->b-<e-",
            "o1 l16 dd>d<dga>cd<ff>f<fff>f<f b-b->b-<b-b-b->b-<b-aa>a<a>g<a>a<add>d<dga>cd<ff>f<fff>f<f b-b->b-<b-b-b->b-<baa>a<a>aec+<a",
            "o1 l16 dr8dr8>cd<rdfde-e-gb- dr8dr8>cdr<dfdccec o1 dr8dr8>cdr<dfde-e-gb- o1 dr8dr8>cdr<dfdccec",
            "@0 q5 v7 o0l16 aaaa>c+<a>d<a>e<a>f<a>g<a>f<a >e<a>f<a>e<a>d<a>c+<abgab>c<b",
            "o0 l16 aaarr8>a8a<aaraa>c+d< aaarr8>a8a<aaraa>c+d< aaarr8>a8a<aaraa>c+d< aaarr8>a8<aa>a<ab-b->c+c+",
            "o1 l16 dddddddddddddddd cccccccccccccccc o0 l16 b-b->fb->d<b-fb-ccg>cec<g>c <ddfa>d<afd<a>age<aaaa> dddddddddddddddd o1 l16 cccccccccccccccc <b-b->fb->d<b-fb- ccg>cec<g>c",
            "o1 l16 ddfa>d<afd <a>age<aaaa",
            "o1 l16 dddddddddddddddd cccccccccccccccc o0 l16 b-b->fb->d<b-fb-ccg>cec<g>c <ddfa>d<afd<a>age<aaaa> dddddddddddddddd o1 l16 cccccccccccccccc <b-b->fb->d<b-fb- ccg>cec<g>c",
            "o1 l16 e-e-b-e-ge-ae- b-e->e-<e->g<e->b-<e-",
            "o1 l16 dd>d<dga>cd&d4r4",
            "r1r1"
        ]
        
        prelude_ch7 = [
            envelope,
            "x4 @3 l16 o0 q2 r2r4r fo4c8",
            
        ]
        melody_ch7 = [
            envelope,
            "x4 @3 l16 o0 q2 l16 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8o0",
            "l16 o0frro4co0fo4co0ff o0frro4co0fo4co0ff o0frro4co0fo4co0ff o0frro4co0fo4ccc o0frro4co0fo4co0ff o0frro4co0fo4co0ff o0frro4co0fo4co0ff fo4ccccccc",
            "l16 o0 fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4crcccc o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0",
            "l16 o0fro4cr o0fro4cr o0fo4cco0fo4cco0fo4c",
            "l16 o0 fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4crcccc o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0",
            "l16 o0 fro4cr o0fro4cr o0fo4ece l32dddd<<aaaa",
            "l16 o0 fro4cro0fro4cro0fro4cro0fro4cro0 fro4cro0fro4cro0fro4cro0fro4cro0 fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4crcccc",
            "l16 o0 frrfrro4c8o0ffo4co0fffo4co0f frrfrro4c8o0ffo4co0fffo4co0f frrfrro4c8o0ffo4co0fffo4co0f frrfrro4c8o0ffo4co0ffo4ccco0",
            "x4 @3 l16 o0 q2 l16 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8 o0ffo4c8o0",
            "l16 o0frro4co0fo4co0ff o0frro4co0fo4co0ff o0frro4co0fo4co0ff o0frro4co0fo4ccc o0frro4co0fo4co0ff o0frro4co0fo4co0ff o0frro4co0fo4co0ff fo4ccccccc",
            "l16 o0 fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4crcccc o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0",
            "l16 o0fro4cr o0fro4cr o0fo4cco0fo4cco0fo4c",
            "l16 o0 fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4crcccc o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0 o0fro4cro0fro4cro0fro4cro0fro4cro0",
            "l16 o0 fro4cr o0fro4cr o0fo4ece l32dddd<<aaaa",
            "l16 o4co0ffo4co0ffo4cco0f8r8r4.",
            "r1r1"
        ]

        pyxel.sounds[0].mml("".join(prelude_ch1))
        pyxel.sounds[1].mml("".join(prelude_ch2))
        pyxel.sounds[2].mml("".join(prelude_ch3))
        pyxel.sounds[3].mml("".join(prelude_ch4))
        pyxel.sounds[4].mml("".join(prelude_ch5))
        pyxel.sounds[5].mml("".join(prelude_ch6))
        pyxel.sounds[6].mml("".join(prelude_ch7))
        # pyxel.sounds[6].set_tones("4")
        pyxel.sounds[10].mml("".join(melody_ch1))
        pyxel.sounds[11].mml("".join(melody_ch2))
        pyxel.sounds[12].mml("".join(melody_ch3))
        pyxel.sounds[13].mml("".join(melody_ch4))
        pyxel.sounds[14].mml("".join(melody_ch5))
        pyxel.sounds[15].mml("".join(melody_ch6))
        pyxel.sounds[16].mml("".join(melody_ch7))
        pyxel.musics[0].set([0],[1],[2],[3],[4],[5],[6])
        pyxel.musics[1].set([10],[11],[12],[13],[14],[15],[16])
        pyxel.run(self.update, self.draw)

    def update(self):
        self.bgm.playing()
    
    def draw(self):
        pyxel.cls(1)
        pyxel.text(14, 60, "TO MAKE THE END OF BATTLE", 7)
            
if __name__ == "__main__":
    App()
