#include "lib/Card.h"

using namespace std;

Card::Card(int id, string name){
	card_ID = id;
	card_name = name;
}//end of constructor

Card::Card(const Card &other) card_ID(other.card_ID), card_name(other.card_name){

}//end of deep constructor

Card::~Card(){
	card_ID = 0;
	card_name = "";
}//end of destructor

string Card::getName() const{
	return card_name;
}//end of getname

int Card::getID() const{
	return card_ID;
}//end of getID

void Card::printCard() const{
	cout << card_name << "  --  " << card_ID << endl;
}//end of printing 