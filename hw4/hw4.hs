import System.Random (randomRIO)
    
data Game = Game {word :: String, display :: String} deriving (Show)

main :: IO ()
main=do dict<-readFile "words.txt"
        let theLines=lines dict
        let theWords=map words theLines
        let len=length theLines
        randomNum <- randomRIO(0,9999999 :: Int)
        let index=randomNum `mod` len
        let randomWord=(theWords!!index)!!0
        let myGame=Game randomWord (map (\_->'_') [0..((length randomWord)-1)])
        loop2 myGame
        


loop2 :: Game -> IO ()
loop2 myGame=do putStrLn (display myGame)
                myLine<-getLine
                let c=if (null myLine) then '\n' else (head myLine)
                let newDisplay = (map (\currentChar->if currentChar==c
                                                       then c
                                                       else '_') (word myGame))
                let finalDisplay=(map (\index->if newDisplay!!index /= '_'
                                                 then newDisplay!!index
                                                 else (display myGame)!!index) [0..((length (word myGame))-1)])
                if any ('_'==) (finalDisplay)
                  then loop2 (Game (word myGame) finalDisplay)
                  else putStrLn finalDisplay

