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

#verze z 2.10.2014
# aby mi fungovalo strobe off i bez odpovedi, musel jsem vrati ISI 0.1 s po krizku
from ctypes import windll #kamil
pport = windll.inpout32
pport_addrr = 0x2FF8 #0x0378 - pocitac #0x2FF8 - notebook
pport.Out32(pport_addrr, 4) # sets pin no.3 to high
pport.Out32(pport_addrr+2, 0) # strobe off  

# Store info about the experiment session
expName = 'PPAlocalizerEEG'  # from the Builder filename that created this script
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

# Initialize components for Routine "pauza"
pauzaClock = core.Clock()
krizek_pauza = visual.ImageStim(win=win, name='krizek_pauza',
    image='imagesFMRI/cross.jpg', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
krizek = visual.ImageStim(win=win, name='krizek',
    image='imagesFMRI/cross.jpg', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)

# Initialize components for Routine "pauza2"
pauza2Clock = core.Clock()
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions('PPAconditionsEEG.csv'),
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
        routineTimer.add(3.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        pauzaComponents = []
        pauzaComponents.append(krizek_pauza)
        for thisComponent in pauzaComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "pauza"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = pauzaClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *krizek_pauza* updates
            if t >= 2.0 and krizek_pauza.status == NOT_STARTED:
                # keep track of start time/frame for later
                krizek_pauza.tStart = t  # underestimates by a little under one frame
                krizek_pauza.frameNStart = frameN  # exact frame index
                krizek_pauza.setAutoDraw(True)
            elif krizek_pauza.status == STARTED and t >= (2.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
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
        
        #-------Ending Routine "pauza"-------
        for thisComponent in pauzaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed pauza repeats of 'pauza_loop'
    
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    image.setImage('imagesFMRI/'+obrazek)
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
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            #kamil
            pport.Out32(pport_addrr, 255) # sets all pins to low
            pport.Out32(pport_addrr+2, 1) # strobe on
            
        elif image.status == STARTED and t >= (0.0 + (.2-win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)
        
        # *odpoved* updates
        if t >= 0.0 and odpoved.status == NOT_STARTED:
            # keep track of start time/frame for later
            odpoved.tStart = t  # underestimates by a little under one frame
            odpoved.frameNStart = frameN  # exact frame index
            odpoved.status = STARTED
            # keyboard checking is just starting
            odpoved.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        elif odpoved.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            odpoved.status = STOPPED
        if odpoved.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                odpoved.keys = theseKeys[-1]  # just the last key pressed
                odpoved.rt = odpoved.clock.getTime()
                # was this 'correct'?
                if (odpoved.keys == str(corrans)) or (odpoved.keys == corrans):
                    odpoved.corr = 1
                else:
                    odpoved.corr = 0
                # a response ends the routine
                #continueRoutine = False
                #kamil
                #odpoved v tehle verzi nekonci trial
                pport.Out32(pport_addrr, 4) # sets pin no.3 to high
                pport.Out32(pport_addrr+2, 0) # strobe off
        
        # *krizek* updates
        if t >= 0.2 and krizek.status == NOT_STARTED:
            # keep track of start time/frame for later
            krizek.tStart = t  # underestimates by a little under one frame
            krizek.frameNStart = frameN  # exact frame index
            krizek.setAutoDraw(True)
        elif krizek.status == STARTED and t >= (0.2 + (0.8-win.monitorFramePeriod*0.75)): #most of one frame period left
            krizek.setAutoDraw(False)
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
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if odpoved.keys in ['', [], None]:  # No response was made
       odpoved.keys=None
       # was no response the correct answer?!
       if str(corrans).lower() == 'none': odpoved.corr = 1  # correct non-response
       else: odpoved.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('odpoved.keys',odpoved.keys)
    trials.addData('odpoved.corr', odpoved.corr)
    if odpoved.keys != None:  # we had a response
        trials.addData('odpoved.rt', odpoved.rt)
    
    #------Prepare to start Routine "pauza2"-------
    t = 0
    pauza2Clock.reset()  # clock 
    frameN = -1
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pauza2Components = []
    pauza2Components.append(ISI)
    for thisComponent in pauza2Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pauza2"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauza2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.1)
            #if len(theseKeys) == 0: #nestlacil klavesu
            #pokud nestlacil klavesu, musim dat stejne strobe off  - 1.10.2014
            pport.Out32(pport_addrr, 4) # sets pin no.3 to high
            pport.Out32(pport_addrr+2, 0) # strobe off
        elif ISI.status == STARTED: #one frame should pass before updating params and completing
            ISI.complete() #finish the static period
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineTimer.reset()  # if we abort early the non-slip timer needs reset
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauza2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pauza2"-------
    for thisComponent in pauza2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

win.close()
core.quit()
