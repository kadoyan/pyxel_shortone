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
            pyxel.playm(self.melody, loop=True)

class App:
    def __init__(self):
        pyxel.init(128, 128, display_scale=2, fps=60)
        self.bgm = PreludeMusic(0,1)
        pyxel.run(self.update, self.draw)

    def update(self):
        envelope = "x0:77776767656545454343232121 x1:6666565645454534342121 x2:45454543 x3:665543 x4:67777665544321"
        prelude_ch1 = [
            envelope,
            "t140 @2 o3 q7 x0 r2",
            "l8 eefgrgrgccderere",
            "l4 <aa>dcl16q8<b&>c&<&b>c&<b&>c&<b&>c&<b&>c&<b&>cl8<a&b",
            "x0 v7 >c& x0 c2< q6 x3 f4fe4.f4fe4",
            "q7 x0 >c& x0 c2< q6 x3 f4fe4.f4fe4"
        ]
        melody_ch1 = [
            envelope,
            "t140 @2 o3 q7 x4",
            "l4 rde.dd8ede",
            "l8 f4e x0 c&c2< @0 x3 f4ec4fe x0 c&", 
            "c @2 r>l4de.dd8ede",
            "l8 ffffrfedccdcr<b>cd",
            "@1 l4 <b.>c.d.<bl8b>e.d.c",
            "<bl4>c<b.a8g8a.b.>c",
            "@2 l8 r<fa>ced4cl16q5ded8cdc8<b>c<b8aba8",
            "q7l8g4.a&a2b2r>gfe"
        ]
        
        prelude_ch2 = [
            envelope,
            "t140 @1 o3 q7 x4 r2",
            "l8ccderere<aab>crcrc",
            "l4<ffaaf2~&f~l8fg",
            "e2&e~q6v5c4cc4.c4cc4q7",
            "e2&e~q6v5c4cc4.c4cc4"
        ]
        melody_ch2 = [
            envelope,
            "t140 @1 o3 q7 x1",
            "l4 r<b>c.<bb8>c<b>c",
            "l8 d4c<a&a2 @1 x3 f4ec4fec8&",
            "c x1 @1 r>l4<b>c.<bb8>c<b>c",
            "l8<bbbbrbbbaabarb>cd",
            "<l4e.e.g.el8e> c.<b.g",
            "el4ag.e8e8e.g.a",
            "l8rf4f>c<b4al16b>c<b8aba8gag8fgf8",
            "l8d4.e&e2f2r>edc"
        ]
        
        prelude_ch3 = [
            envelope,
            "t140 @0 o1 q5 x3 r2",
            "l4cr2c<ar2a",
            "l8f.r.ff.r.fg.r.gg.r.g",
            ">cc>c<ccc>c<ccc>c<ccc>c<c",
            "cc>c<ccc>c<ccc>c<ccc>c<c"
        ]
        melody_ch3 = [
            envelope,
            "t140 @0 o1 q5 x3",
            "cc>c<ccc>c<ccc>c<ccc>c<c",
            "<aa>a<aaa>a<aaa>a<aaa>a<a",
            "ff>f<fff>f<fff>f<fff>f<f",
            "gg>g<ggg>g<ggg>g<ggg>a<b",
            ">c>c<c>c<c>c<c>c<c>c<c>c<c>c<c>c<",
            "<a>a<a>a<a>a<a>a<a>a<a>a<a>a<a>a",
            "<f>f<f>f<f>f<f>f<f>f<f>f<f>f<f>f",
            "rggrrggrrggga4g4"
        ]
        prelude_ch4 = [
            envelope,
            "t140 @3 o4 q1 v2 r2",
            "l8 b r2 o0q1co4 bbbr2 o0q1co4 bb",
            "br o0q1co4 bb r o0q1co4 bb r o0q1co4 bb r o0q1co4 b",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3",
        ]
        melody_ch4 = [
            envelope,
            "t140 @3 o4 q1 v2 l8",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bo4v3 bb l16bb l8",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3",
            "o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bbo4v3 b o4v1bo4v3 o4v1bo4v3 bb l16bb",
        ]

        pyxel.sounds[0].mml("".join(prelude_ch1))
        pyxel.sounds[1].mml("".join(prelude_ch2))
        pyxel.sounds[2].mml("".join(prelude_ch3))
        pyxel.sounds[3].mml("".join(prelude_ch4))
        pyxel.sounds[4].mml("".join(melody_ch1))
        pyxel.sounds[5].mml("".join(melody_ch2))
        pyxel.sounds[6].mml("".join(melody_ch3))
        pyxel.sounds[7].mml("".join(melody_ch4))
        pyxel.musics[0].set([0],[1],[2],[3])
        pyxel.musics[1].set([4],[5],[6],[7])
        self.bgm.playing()
    
    def draw(self):
        pyxel.cls(12)
        pyxel.text(25, 50, "Esper Dream NANOSA", 7)
        pyxel.text(25, 58, "play_pos:"+str(pyxel.play_pos(0)[1]), 5)
            
if __name__ == "__main__":
    App()
