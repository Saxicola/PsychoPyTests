#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.03), 2014_10_02_1038
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import serial
from Arduino import * #lukas

#verze z 2.10.2014
# aby mi fungovalo strobe off i bez odpovedi, musel jsem vrati ISI 0.1 s po krizku

arduino = Arduino()
arduino.connect()
print arduino.is_open()
arduino.blink()
arduino_up = False; #status, jestli posledni puls nahoru

blokcislo = 0;
ovocebylo = 0;
ovocenalezeno = 0;
reakcecas = 0;
chciklavesu_default = 1; #jestli budu vyzadovat klavesy
chciklavesu = chciklavesu_default;

# Store info about the experiment session
expName = 'PPAlocalizerEEG_LPT2016-10'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
if expInfo['session']== '1':
    csvfile = 'PPAconditionsEEG2016-10-24a.csv'
    celkembloku = 66; #prvni cast souboru
elif expInfo['session']== '2':
    csvfile = 'PPAconditionsEEG2016-10-24b.csv'
    celkembloku = 64; #druha cast souboru
else:
    csvfile = 'PPAconditionsEEG2016-10-24.csv'
    celkembloku = 130; #cely soubor
print 'csvfile: ' + csvfile    
    

# Setup filename for saving
filename = 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1600, 900), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "pauza"
pauzaClock = core.Clock()
krizek_pauza = visual.ImageStim(win=win, name='krizek_pauza',
    image='imagesFMRI2016/cross.jpg', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
#text napovedy -   25.1.2016  =====================================
text4 = visual.TextStim(win=win, ori=0, name='text4',
    text='default text',    font='Arial',
    pos=[0, -0.75], height=0.07, wrapWidth=None,
    color='blue', colorSpace='rgb', opacity=1,
    depth=-3.0)
#text stlaceni klavesy -   17.3.2017  ====================================    
text5 = visual.TextStim(win=win, ori=0, name='text2',
    text=u'Zm\xe1\u010dkn\u011bte \u0161ipku doprava pro pokra\u010dov\xe1n\xed',    font='Arial',
    pos=[0, -0.9], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
        
# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
krizek = visual.ImageStim(win=win, name='krizek',
    image='imagesFMRI2016/cross.jpg', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)

# Initialize components for Routine "pauza2"
pauza2Clock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Initialize components for Routine "cekejdlouho"
cekejdlouhoClock = core.Clock()
text_cekejdlouho = visual.TextStim(win=win, ori=0, name='text_cekejdlouho',
    text='default text',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'white', colorSpace=u'rgb', opacity=1,
    depth=0.0)
    
# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(csvfile),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    
    # set up handler to look after randomisation of conditions etc
    pauza_loop = data.TrialHandler(nReps=pauza, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='pauza_loop')
    thisExp.addLoop(pauza_loop)  # add the loop to the experiment
    thisPauza_loop = pauza_loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisPauza_loop.rgb)
    if thisPauza_loop != None:
        for paramName in thisPauza_loop.keys():
            exec(paramName + '= thisPauza_loop.' + paramName)
    
    for thisPauza_loop in pauza_loop:
        currentLoop = pauza_loop
        # abbreviate parameter names if possible (e.g. rgb = thisPauza_loop.rgb)
        if thisPauza_loop != None:
            for paramName in thisPauza_loop.keys():
                exec(paramName + '= thisPauza_loop.' + paramName)
        
        #------Prepare to start Routine "pauza"-------
        t = 0
        pauzaClock.reset()  # clock 
        frameN = -1
        frameNklavesa = 0
        
        blokcislo += 1
        
        # update component parameters for each repeat
        # keep track of which components have finished
        pauzaComponents = []
        pauzaComponents.append(krizek_pauza)
        textScore = 'blok ' + str(blokcislo) + '/' + str(celkembloku)
        textScore += '\novoce/zelenina: ' + str(ovocenalezeno) + '/' + str(ovocebylo)
        if reakcecas > 0: 
            textScore +=  '\ncas reakce: ' + ( "%.0f" %  (reakcecas*1000) ) + ' ms'
        elif reakcecas == -1:
            textScore +=  '\npropasli jste ovoce nebo zeleninu'
        
        text4.setText(textScore)
        reakcecas = 0; #hodnotu vynuluju pred dalsim blokem
        pauzaComponents.append(text4)
        #kamil 17.3.2017 - kopiruju stlaceni klavesy z Aedist
        respNapoveda = event.BuilderKeyResponse()  # create an object of type KeyResponse
        respNapoveda.status = NOT_STARTED
        pauzaComponents.append(respNapoveda)
        if chciklavesu:
            pauzaComponents.append(text5)
        for thisComponent in pauzaComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "pauza"-------
        continueRoutine = True        
        while continueRoutine  > 0:
            # get current time
            t = pauzaClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
                                
            # *text4* updates  - cislo bloku a vysledky predchoziho bloku
            if t >= 0.0 and text4.status == NOT_STARTED:
                # keep track of start time/frame for later
                text4.tStart = t  # underestimates by a little under one frame
                text4.frameNStart = frameN  # exact frame index
                text4.setAutoDraw(True)
            elif text4.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)) and respNapoveda.status == FINISHED: #most of one frame period left
                text4.setAutoDraw(False)
            
            # *text5* updates  - stisknete sipku doprava
            if t >= 0.0 and chciklavesu and text5.status == NOT_STARTED :
                # keep track of start time/frame for later
                text5.tStart = t  # underestimates by a little under one frame
                text5.frameNStart = frameN  # exact frame index                
                text5.setAutoDraw(True)
            elif text5.status == STARTED and t >= (0.0 + (2.0-win.monitorFramePeriod*0.75)) and respNapoveda.status == FINISHED: #most of one frame period left
                text5.setAutoDraw(False) 
                
             # *respNapoveda* updates
            if t >= 0.0 and respNapoveda.status == NOT_STARTED:
                # keep track of start time/frame for later
                respNapoveda.tStart = t  # underestimates by a little under one frame
                respNapoveda.frameNStart = frameN  # exact frame index
                if chciklavesu:
                    respNapoveda.status = STARTED
                else:
                    respNapoveda.status = FINISHED #komponenta se nema spustit
                # keyboard checking is just starting
                respNapoveda.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if respNapoveda.status == STARTED:
                theseKeys = event.getKeys(keyList=['right'])  
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    respNapoveda.keys = theseKeys[-1]  # just the last key pressed
                    respNapoveda.rt = respNapoveda.clock.getTime()
                    # a response ends the routine
                    continueRoutine = True
                    respNapoveda.status = FINISHED #sama se asi nenastavi FINISHED, musim rucne
                    chciklavesu = 0; #zatim nechci dalsi klavesu
                    
            if respNapoveda.status != FINISHED: 
                frameNklavesa = frameN
            
            # *krizek_pauza* updates
            if frameN >= frameNklavesa+120 and krizek_pauza.status == NOT_STARTED :
                # keep track of start time/frame for later
                krizek_pauza.tStart = t  # underestimates by a little under one frame
                krizek_pauza.frameNStart = frameN  # exact frame index
                krizek_pauza.setAutoDraw(True)
            elif krizek_pauza.status == STARTED and frameN >= (krizek_pauza.frameNStart + 60) and respNapoveda.status == FINISHED: #predelano na frames 60Hz 7.6.2016
                krizek_pauza.setAutoDraw(False)
                    
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pauzaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "pauza"-------
        for thisComponent in pauzaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
                
        # check responses
        if respNapoveda.keys in ['', [], None]:  # No response was made
           respNapoveda.keys=None
           
        thisExp.nextEntry()
        
    # completed pauza repeats of 'pauza_loop'
    
    
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    
    if corrans == 1:
        ovocebylo += 1
    
    
    # update component parameters for each repeat
    image.setImage('imagesFMRI2016/'+obrazek)
    odpoved = event.BuilderKeyResponse()  # create an object of type KeyResponse
    odpoved.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(image)
    trialComponents.append(odpoved)
    trialComponents.append(krizek)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if frameN >= 0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            #kamil
            #pport.Out32(pport_addrr, 255) # sets all pins to low
            #pport.Out32(pport_addrr+2, 1) # strobe on
            arduino.send_pulse_up()
            arduino_up = True
            logging.log(level=logging.DATA, msg='Arduino pulse up')
            
        elif image.status == STARTED and frameN >= (image.frameNStart + 12): #predelano na frames - 7.6.2016
            image.setAutoDraw(False) #po 12frame=200ms schovej obrazek
        
        # *odpoved* updates
        if frameN >= 0 and odpoved.status == NOT_STARTED:
            # keep track of start time/frame for later
            odpoved.tStart = t  # underestimates by a little under one frame
            odpoved.frameNStart = frameN  # exact frame index
            odpoved.status = STARTED
            # keyboard checking is just starting
            odpoved.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif odpoved.status == STARTED and frameN > (odpoved.frameNStart + 60): #konec casu na odpoved
            #cas na odpoved uz vyprsel 60 frames = 1sec
            odpoved.status = STOPPED  #ale krizek je jeste spusten 6 framu, teprve pak zkonci trial
            if arduino_up: 
                arduino.send_pulse_down() #nestacil odpovedet, chci stejne poslat puls down
                arduino_up = False;
                logging.log(level=logging.DATA, msg='Arduino pulse down')
        
        if odpoved.status == STARTED and frameN <= (odpoved.frameNStart + 60): #odpoved je mozna je 1sec=60frame po podnetu
            theseKeys = event.getKeys(keyList=['space'])         
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                odpoved.keys = theseKeys[-1]  # just the last key pressed
                odpoved.rt = odpoved.clock.getTime()
                #print 'odpoved.keys' + odpoved.keys
                # was this 'correct'?
                if corrans==1 and odpoved.keys == 'space' :  #pokud mel stlacit mezernik   
                    odpoved.corr = 1
                    ovocenalezeno += 1
                    reakcecas = odpoved.rt
                else:
                    odpoved.corr = 0
                # a response ends the routine
                #continueRoutine = False
                #kamil
                #odpoved v tehle verzi nekonci trial
                #pport.Out32(pport_addrr, 4) # sets pin no.3 to high
                #pport.Out32(pport_addrr+2, 0) # strobe off
                arduino.send_pulse_down()
                arduino_up = False
                logging.log(level=logging.DATA, msg='Arduino pulse down')
        
        # *krizek* updates
        if frameN >= 12 and krizek.status == NOT_STARTED:
            # keep track of start time/frame for later
            krizek.tStart = t  # underestimates by a little under one frame
            krizek.frameNStart = frameN  # exact frame index
            krizek.setAutoDraw(True)    #po 12framech = 200ms zobraz krizek
        elif krizek.status == STARTED and frameN >= (krizek.frameNStart + 54): #predelano na frames - 7.6.2016
            krizek.setAutoDraw(False)  #po celkove 66frames = 1.1sec chci krizek zase skryt
            continueRoutine = False #kamil - po tehle komponente chci ukoncit, at zmacknul klavesu nebo ne
            
               
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if odpoved.keys in ['', [], None]:  # No response was made
       odpoved.keys=None
       # was no response the correct answer?!
       if str(corrans).lower() == 'none' or corrans==0: 
            odpoved.corr = 1  # correct non-response
       else: 
            odpoved.corr = 0  # failed to respond (incorrectly)
            reakcecas = -1
    # store data for trials (TrialHandler)
    trials.addData('odpoved.keys',odpoved.keys)
    trials.addData('odpoved.corr', odpoved.corr)
    if odpoved.keys != None:  # we had a response
        trials.addData('odpoved.rt', odpoved.rt)
    
    # Calling nextEntry indicates to the ExperimentHandler that the current trial has ended and so further addData() calls correspond to the next trial.
    thisExp.nextEntry() 
    
    if blokkonec > 0 and (blokcislo == 33 or blokcislo ==  66 or blokcislo == 99):
        zbyvarepetic = 120 #vterin do konce pauzy
        chciklavesu = chciklavesu_default; #pauza bude vyzadovat klavesu na konci
        
        # set up handler to look after randomisation of conditions etc
        loopCekejDlouho = data.TrialHandler(nReps=zbyvarepetic, method=u'sequential', 
            extraInfo=expInfo, originPath=None,
            trialList=[None],
            seed=None, name='loopCekejDlouho')
        thisExp.addLoop(loopCekejDlouho)  # add the loop to the experiment
        thisLoopCekejDlouho = loopCekejDlouho.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb=thisLoopCekejDlouho.rgb)
        if thisLoopCekejDlouho != None:
            for paramName in thisLoopCekejDlouho.keys():
                exec(paramName + '= thisLoopCekejDlouho.' + paramName)
        
        for thisLoopCekejDlouho in loopCekejDlouho:
            currentLoop = loopCekejDlouho
            # abbreviate parameter names if possible (e.g. rgb = thisLoopCekejDlouho.rgb)
            if thisLoopCekejDlouho != None:
                for paramName in thisLoopCekejDlouho.keys():
                    exec(paramName + '= thisLoopCekejDlouho.' + paramName)
            
            #------Prepare to start Routine "cekejdlouho"-------
            t = 0
            cekejdlouhoClock.reset()  # clock 
            frameN = -1
            routineTimer.add(1.000000)
            # update component parameters for each repeat
            text_cekejdlouho.setText(u'Pauza je\u0161t\u011b ' + str(zbyvarepetic) + ' s')
            # keep track of which components have finished
            cekejdlouhoComponents = []
            cekejdlouhoComponents.append(text_cekejdlouho)
            for thisComponent in cekejdlouhoComponents:
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            #-------Start Routine "cekejdlouho"-------
            continueRoutine = True
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = cekejdlouhoClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *text_cekejdlouho* updates
                if t >= 0.0 and text_cekejdlouho.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    text_cekejdlouho.tStart = t  # underestimates by a little under one frame
                    text_cekejdlouho.frameNStart = frameN  # exact frame index
                    text_cekejdlouho.setAutoDraw(True)
                elif text_cekejdlouho.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                    text_cekejdlouho.setAutoDraw(False)
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineTimer.reset()  # if we abort early the non-slip timer needs reset
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in cekejdlouhoComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # check for quit (the Esc key)
                if endExpNow or event.getKeys(keyList=["escape"]):
                    core.quit()
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            #-------Ending Routine "cekejdlouho"-------
            for thisComponent in cekejdlouhoComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.nextEntry()
            
            zbyvarepetic = zbyvarepetic - 1
        #konec smycky 60x
        #thisExp.nextEntry()
            
    # konec if cekej dlouho    
    # completed 60 repeats of 'loopCekejDlouho'
    
# completed 1 repeats of 'trials'

win.close()
core.quit()
