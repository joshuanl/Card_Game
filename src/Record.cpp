#include "Record.h"
#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

Record::Record(string deckName){
	this->deckName = deckName;
	overallWins = 0;
	overAllLoss = 0;
}//end of constructor

Record::~Record(){
	deckName = 0;
	history_map.clear();
}//end of destructor

void Record::printRecord() const{
	cout << endl << " >> Record:  [" << deckName << "]  -- " << overallWins << "-" << overAllLoss << endl;
}//end of printing record

void Record::printRecord(string opponentName) const{
	iterator it = history_map.find(opponentName);
	cout << " >> Record: [" << deckName << "] <<";
	cout << (it->second).opponentName << " -- [" << (it->second).opponentDeckName << "]" << endl;
	cout << "Fought: " << (it->second).fightCount  << endl;
	cout << (it->second).win << " wins   " << (it->second).win << " losses " << endl;
}//end of printing record;

bool Record::recordExists(string opponentName) const{
	iterator it = history_map.find(opponentName);
	if (it == history_map.end()){
		return false;
	}
	return true;
}//end of exists func

void Record::updateRecord(string opponentName, int result){
	iterator it = history_map.find(opponentName);
	(it->second).fightCount++;
	if (result == 1){
		(it->second).win++
		return;
	}
	(it->second).loss++;
}//end of update 

void Record::createNewRecord(string opponentName, string opponentDeckName, int result){
	MatchRecord temp;
	temp.opponentName = opponentName;
	temp.opponentDeckName = opponentDeckName;
	temp.fightCount = 1;
	if (result == 1){
		temp.win = 1;
		temp.loss = 0;
	}
	else{
		temp.win = 0;
		temp.loss = 1;
	}
	history_map.insert(opponentName, temp);
}//end of creating a new record