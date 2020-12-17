module Cauchy where

    data CauchyList = CauchyList Int [Int]

    instance Eq CauchyList where
        (CauchyList p1 list1) == (CauchyList p2 list2) = (p1 == p2) && (sameLists list1 list2)
        -- Implement Eq type class here

    instance Num CauchyList where
        (CauchyList p1 list1) + (CauchyList p2 list2) = let p = max p1 p2 in CauchyList p (addList list1 list2 [] p )   
        (CauchyList p1 list1) - (CauchyList p2 list2) = let p = max p1 p2 in CauchyList p (addList list1 (map (\x -> -x) list2) [] p )
        (CauchyList p1 list1) * (CauchyList p2 list2) = do
            let p = max p1 p2
            let indexList = [0,1..((length list1)+(length list2)-2)]
            CauchyList p (map (\x -> multListOnIndex list1 list2 x p (length indexList)) indexList )
        abs (CauchyList p list) = CauchyList p (map (\x -> abs x) list)
        signum (CauchyList p list) = CauchyList p (map (\x -> signum x) list)
        fromInteger i = let a = (fromInteger i) in CauchyList ( -1 ) [ a ]
        -- Implement Num type class here
        
    instance Show CauchyList where 
        show (CauchyList p list) = "p:" ++ (show p) ++ "\nlength:" ++ (show (length list)) ++ "\ncontent:" ++ (show list)
        --Implement Show type class here

    myFrom i = let a = (fromInteger i) in CauchyList ( (abs a)+1) [abs a]

    safeMod value modVal = do
        if modVal == -1 then value
        else mod value modVal 

    addList list1 list2 buildList modVal = do
        if null list1 && null list2 then buildList
        else if null list1 then (addList list1 (tail list2) (buildList ++ [(safeMod (head list2) modVal)]) modVal)
        else if null list2 then (addList (tail list1) list2 (buildList ++ [(safeMod (head list1) modVal)]) modVal)
        else (addList (tail list1) (tail list2) (buildList ++ [ (safeMod ((head list1) + (head list2)) modVal)]) modVal)

    multListOnIndex list1 list2 index modVal listPadLength = do
        if length list1 < listPadLength then multListOnIndex (list1++[0]) list2 index modVal listPadLength
        else if length list2 < listPadLength then multListOnIndex list1 (list2++[0]) index modVal listPadLength
        else multListCropAndCalc list1 list2 index modVal

    multListCropAndCalc list1 list2 index modVal = do
        let l1 = take (index+1) list1
        let l2 = reverse (take (index+1) list2)
        mod (multListCalc l1 l2 0) modVal

    multListCalc list1 list2 sum = do
        if null list1 then sum
        else multListCalc (tail list1) (tail list2) (sum + ((head list1) * (head list2)) )


    sameLists list1 list2 = do
        if null list1 && null list2 then True
        else if null list1 || null list2 then False
        else if (head list1) /= (head list2) then False
        else sameLists (tail list1) (tail list2)