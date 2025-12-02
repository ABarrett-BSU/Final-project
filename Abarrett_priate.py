import simpleGE, pygame, random

class Coin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Coin.png")
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 10
        self.reset()

    def reset(self):
        
        self.y = -self.rect.height // 2 
        self.x = random.randint(0, self.screen.get_width())
        self.dy = random.randint(self.minSpeed, self.maxSpeed)


    def checkBounds(self):
        
        bottom = self.y + self.rect.height / 2
        if bottom > self.screen.get_height():
            self.reset()
            
class Ametrine(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Ametrine.png")  
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 5
        self.reset()

    def reset(self):
        self.y = -self.rect.height // 2
        self.x = random.randint(0, self.screen.get_width())
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        bottom = self.y + self.rect.height / 2
        if bottom > self.screen.get_height():
            self.reset()
        
class Aquamarine(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Aquamarine.png")   
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 5
        self.reset()

    def reset(self):
        self.y = -self.rect.height // 2
        self.x = random.randint(0, self.screen.get_width())
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        bottom = self.y + self.rect.height / 2
        if bottom > self.screen.get_height():
            self.reset()


class Sapphire(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Sapphire.png")   
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 5
        self.reset()

    def reset(self):
        self.y = -self.rect.height // 2
        self.x = random.randint(0, self.screen.get_width())
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        bottom = self.y + self.rect.height / 2
        if bottom > self.screen.get_height():
            self.reset()
            
class Goldcoin(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Goldcoin.png")   
        self.setSize(40, 40)
        self.minSpeed = 3
        self.maxSpeed = 5
        self.reset()
        
    def reset(self):
        self.y = -self.rect.height // 2
        self.x = random.randint(0, self.screen.get_width())
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        bottom = self.y + self.rect.height / 2
        if bottom > self.screen.get_height():
            self.reset()
                      
class Bomb(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Bomb.png")     
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 5
        self.reset()

    def reset(self):
        self.y = -self.rect.height // 2
        self.x = random.randint(0, self.screen.get_width())
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        bottom = self.y + self.rect.height / 2
        if bottom > self.screen.get_height():
            self.reset()


class Skull(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Skull.png")  
        self.setSize(25, 25)
        self.minSpeed = 3
        self.maxSpeed = 5
        self.reset()

    def reset(self):
        self.y = -self.rect.height // 2
        self.x = random.randint(0, self.screen.get_width())
        self.dy = random.randint(self.minSpeed, self.maxSpeed)

    def checkBounds(self):
        bottom = self.y + self.rect.height / 2
        if bottom > self.screen.get_height():
            self.reset()


class Pirate(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Pirate.png")
        self.setSize(90, 90)
        self.x = 320
        self.y = 400
        self.moveSpeed = 15

    def process(self):

        if self.scene.isKeyPressed(pygame.K_LEFT):
            self.x -= self.moveSpeed
        if self.scene.isKeyPressed(pygame.K_RIGHT):
            self.x += self.moveSpeed

        if self.x < 0:
            self.x = 0
        if self.x > self.screen.get_width():
            self.x = self.screen.get_width()


        self.y = 400

class LblScore(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Score: 0"
        self.center = (100, 30)
        
class LblTime(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left: 15"
        self.center = (500, 30)        
        


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("ship.png")
        
        self.sndCoin = simpleGE.Sound("coin.wav")
        self.sndBad = simpleGE.Sound("bad.wav")

        
        self.numCoins = 10
        self.numAmetrine = 3
        self.numSapphire = 3
        self.numAquamarine = 3
        self.numSapphire = 3
        self.numGoldcoin = 1
        self.numBombs = 2
        self.numSkulls = 2
        
        self.score = 0
        self.lblScore = LblScore()
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 15    
        self.timer.start()
        self.lblTime = LblTime()

        self.pirate = Pirate(self)

        self.coins = []
        for i in range(self.numCoins):
            self.coins.append(Coin(self))
          
        self.ametrines = []
        for i in range(self.numAmetrine):
            self.ametrines.append(Ametrine(self))

        self.aquamarines = []
        for i in range(self.numAquamarine):
            self.aquamarines.append(Aquamarine(self))

        self.sapphires = []
        for i in range(self.numSapphire):
            self.sapphires.append(Sapphire(self))
            
        self.goldcoin = []
        for i in range(self.numGoldcoin):
            self.goldcoin.append(Goldcoin(self))
            
        self.bombs = []
        for i in range(self.numBombs):
            self.bombs.append(Bomb(self))

        self.skulls = []
        for i in range(self.numSkulls):
            self.skulls.append(Skull(self))
            
        self.burstBombs = []
        self.burstSkulls = []
        
        self.burstTimer = simpleGE.Timer()
        self.burstTimer.totalTime = random.randint(3, 7)   
        self.burstTimer.start()
        

        self.sprites = [
            self.pirate,
            self.coins,
            self.ametrines,
            self.aquamarines,
            self.sapphires,
            self.goldcoin,
            self.bombs,
            self.skulls,
            self.burstBombs,
            self.burstSkulls,
            self.lblScore,
            self.lblTime,
            ]

                                                        


    def process(self):

       
        if self.burstTimer.getTimeLeft() <= 0:
            burstCount = random.randint(2, 5)
            hazardType = random.choice(["bombs", "skulls", "both"])

            self.burstBombs.clear()
            self.burstSkulls.clear()

            if hazardType in ["bombs", "both"]:
                for _ in range(burstCount):
                    self.burstBombs.append(Bomb(self))

            if hazardType in ["skulls", "both"]:
                for _ in range(burstCount):
                    self.burstSkulls.append(Skull(self))

            self.burstTimer.totalTime = random.randint(3, 7)
            self.burstTimer.start()
            
        
        for coin in self.coins:
            if coin.collidesWith(self.pirate):
                coin.reset()
                self.sndCoin.play()
                self.score += 10

        
        for gem in self.ametrines:
            if gem.collidesWith(self.pirate):
                gem.reset()
                self.sndCoin.play()
                self.score += 20

        for gem in self.aquamarines:
            if gem.collidesWith(self.pirate):
                gem.reset()
                self.sndCoin.play()
                self.score += 25

        for gem in self.sapphires:
            if gem.collidesWith(self.pirate):
                gem.reset()
                self.sndCoin.play()
                self.score += 30
                
        for gem in self.goldcoin:
            if gem.collidesWith(self.pirate):
                gem.reset()
                self.sndCoin.play()
                self.score += 40

        
        for bomb in self.bombs:
            if bomb.collidesWith(self.pirate):
                bomb.reset()
                self.sndBad.play()
                self.score -= 15

        for skull in self.skulls:
            if skull.collidesWith(self.pirate):
                skull.reset()
                self.sndBad.play()
                self.score -= 10

        
        for bomb in self.burstBombs:
            if bomb.collidesWith(self.pirate):
                bomb.reset()
                self.sndBad.play()
                self.score -= 20

        for skull in self.burstSkulls:
            if skull.collidesWith(self.pirate):
                skull.reset()
                self.sndBad.play()
                self.score -= 15
                
            if self.score < 0:
               self.score = 0
                
                
            self.lblScore.text = f"Score: {self.score}"      
            self.lblTime.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
            
            if self.timer.getTimeLeft() < 0:
                print(f"Score: {self.score}")
                self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self, prevScore):
        super().__init__()
        
        self.prevScore = prevScore

        self.setImage("ship.png")
        self.response ="Quit"

        self.directions = simpleGE.MultiLabel()
        self.directions.textLines = [
            "Ahoy, matey! You’re a pirate on a quest for treasure!",
            "Use the LEFT and RIGHT arrow keys to move your pirate.",
            "Catch coins and rare gems (Ametrine, Aquamarine, Sapphire)",
            "to earn big points and hear the sound of gold!",
            "Beware bombs and skulls – especially random hazard bursts!",
            "                                                          ",            
            ]
        
        self.directions.center = (320, 350)
        self.directions.size = (650, 350)
        self.directions.fontSize = 5
        self.directions.lineSpacing = 1
        
        
        self.btnPlay = simpleGE.Button()
        self.btnPlay.text = "Play"
        self.btnPlay.center = (100, 25)

        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit"
        self.btnQuit.center = (500, 25)
        
        self.lblScore = simpleGE.Label()
        self.lblScore.text = "Last score: 0"
        self.lblScore.center = (300, 25)
        
        self.lblScore.text = f"Last score: {self.prevScore}"

        self.sprites = [self.directions,
                        self.btnPlay,
                        self.btnQuit,
                        self.lblScore]
        
    def process(self):
        if self.btnPlay.clicked:
            self.response = "Play"
            self.stop() 

        if self.btnQuit.clicked:
            self.response = "Quit"
            self.stop() 

def main():
    
    keepGoing = True
    lastScore = 0
            
    while keepGoing:
        instructions = Instructions(lastScore)
        instructions.start()

        if instructions.response == "Play":
            game = Game()
            game.start()
            lastScore = game.score
            
        else:
            keepGoing = False


if __name__ == "__main__":
    main()