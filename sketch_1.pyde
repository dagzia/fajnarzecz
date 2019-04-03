add_library('sound')
add_library('pdf')



def setup():
    global i
    global nazwa
    global ext
    global sf
    nazwa = "id"
    ext = ".jpg"
    i = loadImage("id.jpg")
    #beginRecord(PDF, "mojPDFinny.pdf")-do nagrania
    size(400,400) #, PDF, "mojPDF.pdf")-do zapisania w pdf
    sf = SoundFile(this, "ble.wav")
    imageMode(CENTER)

def draw():
    global i
    global nazwa
    global ext
    image(i, width/2, height/2, width, height) #facet
    if mousePressed: #z kliknięciem pojawia sie devil
        d = loadShape("devil.svg") 
        shape(d, 100, 70, width/2, height/2)
        b = loadShape("widly.svg") #widly
        shape(b, 250, 150, width/2, height/2)
        global sf
        sf.play()
        
    #endRecord()
    #save(nazwa+".edited"+ext)
    #exit()-zamykanie

    
