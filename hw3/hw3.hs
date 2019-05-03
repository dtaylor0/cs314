skips :: [a] -> [[a]]
skips [] = []
skips lst = map (\x -> sublist x lst) [1..length lst]

sublist :: Int -> [a] -> [a]
sublist 0 _ = []
sublist 1 lst = lst
sublist x lst = step 1 x lst
      
step :: Int -> Int -> [a] -> [a]
step _ _ [] = []
step ptr x (i:lst) = if ptr==x then (i:step 1 x lst) else (step (ptr+1) x lst)



localMaxima :: [Integer] -> [Integer]
localMaxima [] = []
localMaxima [i] = []
localMaxima [i,j] = []
localMaxima (i:j:k:lst) = if j>i && j>k then (j:(localMaxima (j:k:lst))) else (localMaxima (j:k:lst))



histogram :: [Integer] -> String
histogram [] = bottomOfHist
histogram lst = (histToString (map (\x -> (toInteger (length (filter (==x) lst)))) [0..9]) 1)++bottomOfHist

histToString :: [Integer] -> Integer -> String
histToString lst num = if ((length (filter (>num) lst))==0) then ((map (\x -> if (x>=num) then '*' else ' ') lst)++"\n") else ((histToString lst (num+1))++(map (\y -> if (y>=num) then '*' else ' ') lst)++"\n")

bottomOfHist :: String
bottomOfHist = "==========\n0123456789"
