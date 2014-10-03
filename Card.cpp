#include "Card.h"
#include <string>

using namespace std;

Card::Card(int id, string name){
	card_ID = id;
	card_name = name;
}//end of constructor

Card::~Card(){
	card_ID = 0;
	card_name = "";
}//end of destructor

string getName() const{
	return card_name;
}//end of getname

int getID() const{
	return card_ID;
}//end of getID