import axelrod as axl
import pprint
import matplotlib.pyplot as plt
from axelrod.graph import Graph
import tkinter as tk
import random
import numpy as np
import csv
import sys 
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from uiipd import Ui_Dialog
import PyQt5.Qt
        
class StrategyMenu(QtWidgets.QDialog):
        def __init__(self):
                super(StrategyMenu, self).__init__()
                loadUi('strtgyui.ui', self)
 
class FaqMenu(QtWidgets.QDialog):
        def __init__(self):
                super(FaqMenu, self).__init__()
                loadUi('faq.ui', self)
                 
class GuiMenu(Ui_Dialog):
        def __init__(self, dialog):
                Ui_Dialog.__init__(self)
                self.setupUi(dialog)                    
                self.buttonBox.clicked.connect(dialog.accept)
                self.buttonBox.accepted.connect(self.accept)
                self.buttonBox.rejected.connect(dialog.reject)
                self.strategy_button.clicked.connect(self.executeStrategy)
                self.faq_button.clicked.connect(self.executeFaq)
                
        def executeStrategy(self):
                strategy_menu = StrategyMenu()
                strategy_menu.exec_()
                
        def executeFaq(self):
                faq_menu = FaqMenu()
                faq_menu.exec_()             
        
        def checkInput(self, input_line):
                if input_line is None:
                        input_line = '1' #setting to one to handle errors
                try:
                        input_line = int(input_line)
                except ValueError:
                        print("Couldn't convert string to integer.")
                        input_line = 1
                
                return input_line

        def accept(self):
                sim_length = self.checkInput(self.sim_length_line.text())
                print("Sim Length: " + str(sim_length))
                sim_turns = self.checkInput(self.turn_length_line.text())
                print("Games per Generation: " + str(sim_turns))
                noise = self.checkInput(self.noise_line.text())
                print("Noise: " + str(noise))
                reward = self.checkInput(self.reward_line.text())
                punishment = self.checkInput(self.punishment_line.text())
                sucker = self.checkInput(self.sucker_line.text())
                temptation = self.checkInput(self.temptation_line.text())
                print('T R S P : ' + str(temptation), str(reward), str(sucker), str(punishment))
                player1 = self.comboBox.currentText()
                player1num = self.player1_line.text()
                player2 = self.comboBox_2.currentText()
                player2num = self.player2_line.text()
                player3 = self.comboBox_3.currentText()
                player3num = self.player3_line.text()
                player4 = self.comboBox_4.currentText()
                player4num = self.player4_line.text()
                player5 = self.comboBox_5.currentText()
                player5num = self.player5_line.text()
                player6 = self.comboBox_6.currentText()
                player6num = self.player6_line.text()
                player7 = self.comboBox_7.currentText()
                player7num = self.player7_line.text()
                player8 = self.comboBox_8.currentText()
                player8num = self.player8_line.text()
                player9 = self.comboBox_9.currentText()
                player9num = self.player9_line.text()
                player10 = self.comboBox_10.currentText()
                player10num = self.player10_line.text()
                print(player1, player2, player3, player4, player5,
                                                      player6, player7, player8, player9, player10)
                print(player1num, player2num, player3num, player4num, player5num, player6num,
                      player7num, player8num, player9num, player10num)
                csv_bool = self.csv_check.isChecked()
                graphs_bool = self.graphs_check.isChecked()
                pop_map_bool = self.pop_map_check.isChecked()
                moran_bool = self.moran_check.isChecked()
                eco_bool = self.eco_check.isChecked()
                tour_bool = self.tour_check.isChecked()
                
                print(csv_bool,graphs_bool,pop_map_bool, moran_bool, eco_bool, tour_bool)
                gamePlayers = [player1, player2, player3,
                                                               player4, player5, player6, player7, player8, player9, player10]
                playerNums = [int(player1num), int(player2num), int(player3num), int(player4num), int(player5num), int(player6num),
                      int(player7num), int(player8num), int(player9num), int(player10num)]

                runSim(sim_length, sim_turns, noise, reward, punishment, sucker, temptation, csv_bool,
                                                       graphs_bool, pop_map_bool, gamePlayers, playerNums, 
                                                       moran_bool, eco_bool, tour_bool)

def evaluatePlayers(gamePlayers, playerNums):
        playerList = []
        for player in gamePlayers:
                print(player)
                if (player == 'Cooperator'):
                        for i in range(playerNums[0]):
                                playerList.append(axl.Cooperator())
                if (player == 'Defector'):
                        for i in range(playerNums[1]):                        
                                playerList.append(axl.Defector())
                if (player == 'Tit For Tat'):
                        for i in range(playerNums[2]):                        
                                playerList.append(axl.TitForTat())
                if (player == "Tit for Two Tats"):
                        for i in range(playerNums[3]):                        
                                playerList.append(axl.DynamicTwoTitsForTat())
                if (player == 'Grudger'):
                        for i in range(playerNums[4]):                        
                                playerList.append(axl.Grudger())  
                if (player == 'Revised Downing'):
                        for i in range(playerNums[5]):                        
                                playerList.append(axl.RevisedDowning(revised=True))   
                if (player == 'Nydegger'):
                        for i in range(playerNums[6]):                        
                                playerList.append(axl.Nydegger())
                if (player == 'Copier'):
                        for i in range(playerNums[7]):                        
                                playerList.append(axl.AverageCopier())
                if (player == 'Pavlov'):
                        for i in range(playerNums[8]):                        
                                playerList.append(axl.APavlov2011())
                if (player == 'Random'):
                        for i in range(playerNums[9]):                        
                                playerList.append(axl.Random())
        print(playerList)
        gamePlayers = np.array([playerList])
        gamePlayers = gamePlayers.flatten()
        print(gamePlayers)                              

        return gamePlayers        

def runEco(playerList, payoffs, num_games_generation, sim_length, pop_map_bool, graph_bool, csv_bool):
        ecoTournament = axl.Tournament(players=playerList, game=payoffs, turns=num_games_generation, repetitions=sim_length)
        results = ecoTournament.play()
        eco = axl.Ecosystem(results)
        eco.reproduce(sim_length) #generations
        
        if pop_map_bool == True:
                plot = axl.Plot(results)
                
                p = plot.stackplot(eco, title="Eco: Strategy Sustainability over Time") #Colored chart that shows wins through generations
                p.show() 
                
        #if graph_bool == True:
                ##r = plot.boxplot(eco) #Shows distribution of wins through generations        
                ##s = plot.boxplot(eco) #Shows total wins between games
                ##t = plot.pdplot(eco) #shows matrices of results between two sets of different strategies
                ##u = plot.sdvplot(eco) 
                
                #r.show()
                ##t.show()

def runTour(playerList, payoffs, num_games_generation, sim_length, pop_map_bool, graph_bool, csv_bool):
        tournament = axl.Tournament(players=playerList, game=payoffs, turns=num_games_generation, repetitions=sim_length)
        results = tournament.play()
        summary = results.summarise()
        pprint.pprint(summary)
        if csv_bool == True:
                results.write_summary('ipd-sim-results-tour.csv')
        
        if graph_bool == True:
                plot = axl.Plot(results)
                p = plot.boxplot(title="Tournament Results")
               

def runSim(sim_length, sim_turns, noise, reward, punishment, 
           sucker, temptation, csv_bool, graphs_bool, pop_map_bool, gamePlayers, playerNums, moran_bool, eco_bool, tour_bool):
        simPlayers = evaluatePlayers(gamePlayers, playerNums)

        with open('ipd-sim-results.csv', 'w') as csvfile:
                writer = csv.writer(csvfile)
                if csv_bool == True:
                        writer.writerow(["Moran Results"])
                print("Welcome to ipd-sim!")

                temptation = int(temptation)
                sucker = int(sucker)
                reward = int(reward)
                punishment = int(punishment)                                                       
                sim_turns = int(sim_turns)
                noise = float(noise)
                #num_generations = int(num_generations)
                if csv_bool == True:
                        writer.writerow(["Reward: "+str(reward)+" Temptation: "+str(temptation)+" Sucker: "+ str(sucker)+" Punishment: "+str(punishment)])
                        writer.writerow(["Number of turns: "+str(sim_turns)])
                        writer.writerow(["Noise variable: "+str(noise)])                
                        writer.writerow(["Starting Players: "+str(simPlayers)])
                        
                #axl.seed(0) #Limit against unpredictable behavior 
                payoffs = axl.game.Game(r=reward,s=sucker,t=temptation,p=punishment)
                
                if moran_bool == True:
                        mp = axl.MoranProcess(players=simPlayers, turns=sim_turns,game=payoffs,noise=noise)
                        populations = mp.play()
                        print("Moran Winning Strategy: " + mp.winning_strategy_name + "\n") #Display winning strategy
                        if csv_bool == True:
                                writer.writerow([x for x in populations])
                                pprint.pprint(populations) #Print results 
        
                        counter = 0
                        for row in mp.score_history:  
                                print([round(score, 1) for score in row])
                                counter = counter+1
                                if csv_bool == True:
                                        writer.writerows([["Turn #"+str(counter)]])
                                        writer.writerows([[str([round(score, 1) for score in row])]])
                                  
                
                if eco_bool == True:
                        runEco(playerList=simPlayers, payoffs=payoffs, num_games_generation=sim_turns,
                               sim_length=sim_length, pop_map_bool=pop_map_bool, graph_bool=graphs_bool, csv_bool=csv_bool)
                
                if tour_bool == True:
                        runTour(playerList=simPlayers, payoffs=payoffs, num_games_generation=sim_turns,
                               sim_length=sim_length, pop_map_bool=pop_map_bool, graph_bool=graphs_bool, csv_bool=csv_bool)
                        
                if pop_map_bool == True:                        
                        ax = mp.populations_plot()
                        plt.show()
                
if __name__ == '__main__':
        app = QApplication(sys.argv)
        dialog = QtWidgets.QDialog()
        prog = GuiMenu(dialog)
        dialog.show()
        sys.exit(app.exec_())