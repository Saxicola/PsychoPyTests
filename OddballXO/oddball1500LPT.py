#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.03), 2015_10_07_0914
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

from ctypes import windll #kamil
pport = windll.inpout32
pport_addrr = 0x2008 #0x2FF8 #0x0378 - pocitac #0x2FF8 - notebook #0xDC00 - novy experimentalni pocitac
pport_byte0 = 0 #hodnota portu v klidu - pred podnetem a po odpovedi
pport.Out32(pport_addrr, pport_byte0) # sets pin no.3 to high
pport.Out32(pport_addrr+2, 0) # strobe off

# Store info about the experiment session
expName = 'oddball1500'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

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

# Initialize components for Routine "instr"
instrClock = core.Clock()
text_instr = visual.TextStim(win=win, ori=0, name='text_instr',
    text=u'OddBall task\nzm\xe1\u010dkn\u011bte\ndoleva, pokud se zobraz\xed X\ndoprava, pokud se zobraz\xed O\n',    font='Arial',
    pos=[0, 0], height=0.09, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pauzza"
pauzzaClock = core.Clock()
text_pauza = visual.TextStim(win=win, ori=0, name='text_pauza',
    text=u'Mezern\xedk pro pokra\u010dov\xe1n\xed',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
pport_byte = 0
text_trial = visual.TextStim(win=win, ori=0, name='text_trial',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.8, wrapWidth=None,
    color='blue', colorSpace='rgb', opacity=1,
    depth=-2.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instr"-------
t = 0
instrClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_instr = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_instr.status = NOT_STARTED
# keep track of which components have finished
instrComponents = []
instrComponents.append(text_instr)
instrComponents.append(key_resp_instr)
for thisComponent in instrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instr"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instr* updates
    if t >= 0.0 and text_instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instr.tStart = t  # underestimates by a little under one frame
        text_instr.frameNStart = frameN  # exact frame index
        text_instr.setAutoDraw(True)
    
    # *key_resp_instr* updates
    if t >= 0.0 and key_resp_instr.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instr.tStart = t  # underestimates by a little under one frame
        key_resp_instr.frameNStart = frameN  # exact frame index
        key_resp_instr.status = STARTED
        # keyboard checking is just starting
        key_resp_instr.clock.reset()  # now t=0
        event.clearEvents(eventType='keyboard')
    if key_resp_instr.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_instr.keys = theseKeys[-1]  # just the last key pressed
            key_resp_instr.rt = key_resp_instr.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instrComponents:
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

#-------Ending Routine "instr"-------
for thisComponent in instrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_instr.keys in ['', [], None]:  # No response was made
   key_resp_instr.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_instr.keys',key_resp_instr.keys)
if key_resp_instr.keys != None:  # we had a response
    thisExp.addData('key_resp_instr.rt', key_resp_instr.rt)
thisExp.nextEntry()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('oddball.csv'),
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
    trials_pauza = data.TrialHandler(nReps=pauza, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='trials_pauza')
    thisExp.addLoop(trials_pauza)  # add the loop to the experiment
    thisTrials_pauza = trials_pauza.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisTrials_pauza.rgb)
    if thisTrials_pauza != None:
        for paramName in thisTrials_pauza.keys():
            exec(paramName + '= thisTrials_pauza.' + paramName)
    
    for thisTrials_pauza in trials_pauza:
        currentLoop = trials_pauza
        # abbreviate parameter names if possible (e.g. rgb = thisTrials_pauza.rgb)
        if thisTrials_pauza != None:
            for paramName in thisTrials_pauza.keys():
                exec(paramName + '= thisTrials_pauza.' + paramName)
        
        #------Prepare to start Routine "pauzza"-------
        t = 0
        pauzzaClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        key_resp_pauza = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_pauza.status = NOT_STARTED
        # keep track of which components have finished
        pauzzaComponents = []
        pauzzaComponents.append(text_pauza)
        pauzzaComponents.append(key_resp_pauza)
        for thisComponent in pauzzaComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "pauzza"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = pauzzaClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_pauza* updates
            if t >= 0.0 and text_pauza.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_pauza.tStart = t  # underestimates by a little under one frame
                text_pauza.frameNStart = frameN  # exact frame index
                text_pauza.setAutoDraw(True)
            
            # *key_resp_pauza* updates
            if t >= 0.0 and key_resp_pauza.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_pauza.tStart = t  # underestimates by a little under one frame
                key_resp_pauza.frameNStart = frameN  # exact frame index
                key_resp_pauza.status = STARTED
                # keyboard checking is just starting
                key_resp_pauza.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if key_resp_pauza.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_pauza.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_pauza.rt = key_resp_pauza.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pauzzaComponents:
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
        
        #-------Ending Routine "pauzza"-------
        for thisComponent in pauzzaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_pauza.keys in ['', [], None]:  # No response was made
           key_resp_pauza.keys=None
        # store data for trials_pauza (TrialHandler)
        trials_pauza.addData('key_resp_pauza.keys',key_resp_pauza.keys)
        if key_resp_pauza.keys != None:  # we had a response
            trials_pauza.addData('key_resp_pauza.rt', key_resp_pauza.rt)
        thisExp.nextEntry()
        
    # completed pauza repeats of 'trials_pauza'
    
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    if oddball == 1:
        pport_byte = 1 #PIN 1
    else:
        pport_byte = 2 #PIN 2 - je mereny mezi zelenym a zlutym banankem
    
    
    text_trial.setText(text)
    key_resp_trial = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_trial.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(text_trial)
    trialComponents.append(key_resp_trial)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *text_trial* updates
        if t >= 0.5 and text_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_trial.tStart = t  # underestimates by a little under one frame
            text_trial.frameNStart = frameN  # exact frame index
            text_trial.setAutoDraw(True)
            #kamil
            pport.Out32(pport_addrr, pport_byte) # sets all pins to low
            pport.Out32(pport_addrr+2, 1) # strobe on
        elif text_trial.status == STARTED and t >= (0.5 + (0.1-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_trial.setAutoDraw(False)
        
        # *key_resp_trial* updates
        if t >= 0.5 and key_resp_trial.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_trial.tStart = t  # underestimates by a little under one frame
            key_resp_trial.frameNStart = frameN  # exact frame index
            key_resp_trial.status = STARTED
            # keyboard checking is just starting
            key_resp_trial.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif key_resp_trial.status == STARTED and t >= (0.5 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            key_resp_trial.status = STOPPED
            #kamil - jestli nezmacknul klavesu, chci stejne resetovat LPT+++++++++++++++++++++++++++++++
            pport.Out32(pport_addrr, pport_byte0) # sets all pins to low
            pport.Out32(pport_addrr+2, 0) # strobe on
        if key_resp_trial.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if key_resp_trial.keys == []:  # then this was the first keypress
                    key_resp_trial.keys = theseKeys[0]  # just the first key pressed
                    key_resp_trial.rt = key_resp_trial.clock.getTime()
                #kamil
                pport.Out32(pport_addrr, 4) # sets all pins to low
                pport.Out32(pport_addrr+2, 0) # strobe on
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.5)
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
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
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_trial.keys in ['', [], None]:  # No response was made
       key_resp_trial.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_trial.keys',key_resp_trial.keys)
    if key_resp_trial.keys != None:  # we had a response
        trials.addData('key_resp_trial.rt', key_resp_trial.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


win.close()
core.quit()
