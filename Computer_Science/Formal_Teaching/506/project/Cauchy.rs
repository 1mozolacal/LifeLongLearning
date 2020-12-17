use std::fmt;
use std::ops;
use std::cmp;


pub struct CauchyList {
    pub p: i32,
    pub content: Vec<i32>
}

impl CauchyList {
    // CauchyList methods go here, if desired!
    fn safeIndex(&self, index: usize) ->i32{
        if(index >= self.content.len()){
            return 0;
        } else {
            return self.content[index];
        }
    }
    fn modByP(&self, value: i32) -> i32{
        if( value % self.p <0){
            return (value % self.p)+self.p;
        }
        return value % self.p;
    }
}

impl cmp::PartialEq for CauchyList {
    fn eq(&self, other: &Self) -> bool {    
        if( self.p != other.p || self.content.len() != other.content.len() ){
            return false;
        }else{
            for (i,x) in other.content.iter().enumerate(){
                if(*x != self.content[i as usize]){
                    return false;
                }
            } 
            return true;
        }
    }
}

impl ops::Add<CauchyList> for CauchyList {
    type Output = CauchyList;
    fn add(self, other: CauchyList) -> CauchyList {
        let mut returnList = CauchyList {p:self.p, content:Vec::new() }; 
        for x in 0..(cmp::max(self.content.len(),other.content.len())){
            returnList.content.push( returnList.modByP(self.safeIndex(x) + other.safeIndex(x)) );
        }
        return returnList;
        // Implement + operation here
    }
}

impl ops::Sub<CauchyList> for CauchyList {
    type Output = CauchyList;
    fn sub(self, other: CauchyList) -> CauchyList {
        let mut returnList = CauchyList {p:self.p, content:Vec::new() }; 
        for x in 0..(cmp::max(self.content.len(),other.content.len())){
            returnList.content.push( returnList.modByP(self.safeIndex(x) - other.safeIndex(x)) );
        }
        return returnList;
        // Implement - operation here
    }
}

impl ops::Mul<CauchyList> for CauchyList {
    type Output = CauchyList;
    fn mul(self, other: CauchyList) -> CauchyList {
        let mut returnList = CauchyList {p:self.p, content:Vec::new() }; 
        for i in 0..(self.content.len() + other.content.len() - 1){
            let mut sum = 0;
            for x in 0..(i+1){
                sum += ( self.safeIndex(x) * other.safeIndex( (i-x)) );
            } 
            returnList.content.push( returnList.modByP(sum)  );
        }
        return returnList;
        // Implement * operation here
    }
}

impl ops::Mul<i32> for CauchyList {
    type Output = CauchyList;
    fn mul(self, other: i32) -> CauchyList {
        let mut returnList = CauchyList {p:self.p, content:Vec::new() }; 
        for x in 0..(self.content.len()){
            returnList.content.push( returnList.modByP(self.safeIndex(x) * other) );
        }
        return returnList;
        // Implement * operation here
    }
}

impl fmt::Display for CauchyList {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {    
        // Implement print formatting here       
        write!(f,"p:{}\nlength:{}\ncontent:{:?}\n", self.p, self.content.len(), self.content)
    }
}