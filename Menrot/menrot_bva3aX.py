#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), leden 13, 2014, at 12:27
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import visual, core, data, event, logging, sound, gui, parallel
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions

from ctypes import windll #kamil
pport = windll.inpout32

# Store info about the experiment session
expName = 'menrot_bva3a'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup files for saving
if not os.path.isdir('data'):
    os.makedirs('data')  # if this fails (e.g. permissions) we will get error
filename = 'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 800), fullscr=True, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb')
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
instrText = visual.TextStim(win=win, ori=0, name='instrText',
    text=u'Ment\xe1ln\xed rotace prostorov\xfdch sc\xe9n',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Prestavka"
PrestavkaClock = core.Clock()
textPrestavka = visual.TextStim(win=win, ori=0, name='textPrestavka',
    text=u'Stiskn\u011bte MEZERN\xcdK pro za\u010d\xe1tek experimentu',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
image = visual.ImageStim(win=win, name='image',
    image='bva3-315r_1024_512.jpg', mask=None, #kamil
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    texRes=128, interpolate=False, depth=-1.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
text = visual.TextStim(win=win, ori=0, name='text',
    text='nonsense',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "instructions"-------
t = 0
instructionsClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
instrResp = event.BuilderKeyResponse()  # create an object of type KeyResponse
instrResp.status = NOT_STARTED
# keep track of which components have finished
instructionsComponents = []
instructionsComponents.append(instrText)
instructionsComponents.append(instrResp)
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "instructions"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t  # underestimates by a little under one frame
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *instrResp* updates
    if t >= 0.0 and instrResp.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrResp.tStart = t  # underestimates by a little under one frame
        instrResp.frameNStart = frameN  # exact frame index
        instrResp.status = STARTED
        # keyboard checking is just starting
        event.clearEvents()
    if instrResp.status == STARTED:
        theseKeys = event.getKeys()
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineTimer.reset()  # if we abort early the non-slip timer needs reset
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the [Esc] key)
    if event.getKeys(["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
    else:  # this Routine was not non-slip safe so reset non-slip timer
        routineTimer.reset()

#-------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'menrot_bva3A1024.csv'),
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
    prestavkaLoop = data.TrialHandler(nReps=pauza, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='prestavkaLoop')
    thisExp.addLoop(prestavkaLoop)  # add the loop to the experiment
    thisPrestavkaLoop = prestavkaLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisPrestavkaLoop.rgb)
    if thisPrestavkaLoop != None:
        for paramName in thisPrestavkaLoop.keys():
            exec(paramName + '= thisPrestavkaLoop.' + paramName)
    
    for thisPrestavkaLoop in prestavkaLoop:
        currentLoop = prestavkaLoop
        # abbreviate parameter names if possible (e.g. rgb = thisPrestavkaLoop.rgb)
        if thisPrestavkaLoop != None:
            for paramName in thisPrestavkaLoop.keys():
                exec(paramName + '= thisPrestavkaLoop.' + paramName)
        
        #------Prepare to start Routine "Prestavka"-------
        t = 0
        PrestavkaClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        respPrestavka = event.BuilderKeyResponse()  # create an object of type KeyResponse
        respPrestavka.status = NOT_STARTED
        # keep track of which components have finished
        PrestavkaComponents = []
        PrestavkaComponents.append(textPrestavka)
        PrestavkaComponents.append(respPrestavka)
        for thisComponent in PrestavkaComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "Prestavka"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = PrestavkaClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textPrestavka* updates
            if t >= 0.0 and textPrestavka.status == NOT_STARTED:
                # keep track of start time/frame for later
                textPrestavka.tStart = t  # underestimates by a little under one frame
                textPrestavka.frameNStart = frameN  # exact frame index
                textPrestavka.setAutoDraw(True)
            
            # *respPrestavka* updates
            if t >= 0.0 and respPrestavka.status == NOT_STARTED:
                # keep track of start time/frame for later
                respPrestavka.tStart = t  # underestimates by a little under one frame
                respPrestavka.frameNStart = frameN  # exact frame index
                respPrestavka.status = STARTED
                # keyboard checking is just starting
                respPrestavka.clock.reset()  # now t=0
                event.clearEvents()
            if respPrestavka.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                if len(theseKeys) > 0:  # at least one key was pressed
                    respPrestavka.keys = theseKeys[-1]  # just the last key pressed
                    respPrestavka.rt = respPrestavka.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in PrestavkaComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "Prestavka"-------
        for thisComponent in PrestavkaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if respPrestavka.keys in ['', [], None]:  # No response was made
           respPrestavka.keys=None
        # store data for prestavkaLoop (TrialHandler)
        prestavkaLoop.addData('respPrestavka.keys',respPrestavka.keys)
        if respPrestavka.keys != None:  # we had a response
            prestavkaLoop.addData('respPrestavka.rt', respPrestavka.rt)
        thisExp.nextEntry()
        
    # completed pauza repeats of 'prestavkaLoop'
    
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image.setImage(obrazek)
    resp = event.BuilderKeyResponse()  # create an object of type KeyResponse
    resp.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(image)
    trialComponents.append(resp)
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
        if t >= 1 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            #kamil
            pport.Out32(0x378, 255) # sets all pins to low
            pport.Out32(0x378+2, 1) # strobe on
        
        # *resp* updates
        if t >= 1 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t  # underestimates by a little under one frame
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            resp.clock.reset()  # now t=0
            event.clearEvents()
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            if len(theseKeys) > 0:  # at least one key was pressed
                resp.keys = theseKeys[-1]  # just the last key pressed
                resp.rt = resp.clock.getTime()
                # was this 'correct'?
                if (resp.keys == str(corrans)) or (resp.keys == corrans):
                    resp.corr = 1
                else:
                    resp.corr = 0
                #kamil
                pport.Out32(0x378, 4) # sets pin no.3 to high
                pport.Out32(0x378+2, 0) # strobe off
                # a response ends the routine
                continueRoutine = False
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
        
        # check for quit (the [Esc] key)
        if event.getKeys(["escape"]):
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
    if resp.keys in ['', [], None]:  # No response was made
       resp.keys=None
       # was no response the correct answer?!
       if str(corrans).lower() == 'none': resp.corr = 1  # correct non-response
       else: resp.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    
    # set up handler to look after randomisation of conditions etc
    feedbackLoop = data.TrialHandler(nReps=zpetnavazba, method='random', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='feedbackLoop')
    thisExp.addLoop(feedbackLoop)  # add the loop to the experiment
    thisFeedbackLoop = feedbackLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisFeedbackLoop.rgb)
    if thisFeedbackLoop != None:
        for paramName in thisFeedbackLoop.keys():
            exec(paramName + '= thisFeedbackLoop.' + paramName)
    
    for thisFeedbackLoop in feedbackLoop:
        currentLoop = feedbackLoop
        # abbreviate parameter names if possible (e.g. rgb = thisFeedbackLoop.rgb)
        if thisFeedbackLoop != None:
            for paramName in thisFeedbackLoop.keys():
                exec(paramName + '= thisFeedbackLoop.' + paramName)
        
        #------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        if resp.corr:#stored on last run routine
          msg=u'Správně'
        else:
          msg=u'Špatně'
        
        text.setText(msg)
        # keep track of which components have finished
        feedbackComponents = []
        feedbackComponents.append(text)
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "feedback"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # underestimates by a little under one frame
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            elif text.status == STARTED and t >= (0.0 + zpetnavazba):
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the [Esc] key)
            if event.getKeys(["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
            else:  # this Routine was not non-slip safe so reset non-slip timer
                routineTimer.reset()
        
        #-------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed zpetnavazba repeats of 'feedbackLoop'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


win.close()
core.quit()
