#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.80.03), duben 26, 2016, at 11:03
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
import random

# Store info about the experiment session
expName = u'sublim2'  # from the Builder filename that created this script
expInfo = {'participant':'', 'session':'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
random.seed()
bilyvlevo = random.randint(0,1 ) #nahodne urcim, jestli bily ctverec bud pro sipku vlevo nebo vpravo
expInfo['bilyvlevo']=bilyvlevo

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
win = visual.Window(size=(1600, 900), fullscr=True, screen=1,allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "pausa"
pausaClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'Zm\xe1\u010dkn\u011bte mezeru pro pokra\u010dov\xe1n\xed',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
Vsipka=""
cassum=0
sipkay=0
ctverecname = ""
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
image_noise = visual.ImageStim(win=win, name='image_noise',
    image=u'maxresdefault.jpg', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-2.0)
image_noise_inverse = visual.ImageStim(win=win, name='image_noise_inverse',
    image=u'maxresdefault_Inverse.jpg', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-3.0)
text_krizek = visual.TextStim(win=win, ori=0, name='text_krizek',
    text='+',    font='Arial',
    pos=[0, 0], height=0.2, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0)
text_sipka = visual.TextStim(win=win, ori=0, name='text_sipka',
    text='default text',    font='Arial',
    pos=[0,0], height=0.3, wrapWidth=None,
    color=[0.5,0.5,0.5], colorSpace='rgb', opacity=1,
    depth=-5.0)
bilyctverec = visual.ImageStim(win=win, name='bilyctverec',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace=u'rgb', opacity=0.5,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=-7.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method=u'sequential', 
    extraInfo=expInfo, originPath=None,
    trialList=data.importConditions(u'sublim120.csv'),
    seed=1, name='trials')
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
    pausa_if = data.TrialHandler(nReps=pauza, method='sequential', 
        extraInfo=expInfo, originPath=None,
        trialList=[None],
        seed=None, name='pausa_if')
    thisExp.addLoop(pausa_if)  # add the loop to the experiment
    thisPausa_if = pausa_if.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisPausa_if.rgb)
    if thisPausa_if != None:
        for paramName in thisPausa_if.keys():
            exec(paramName + '= thisPausa_if.' + paramName)
    
    for thisPausa_if in pausa_if:
        currentLoop = pausa_if
        # abbreviate parameter names if possible (e.g. rgb = thisPausa_if.rgb)
        if thisPausa_if != None:
            for paramName in thisPausa_if.keys():
                exec(paramName + '= thisPausa_if.' + paramName)
        
        #------Prepare to start Routine "pausa"-------
        t = 0
        pausaClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
        key_resp_2.status = NOT_STARTED
        # keep track of which components have finished
        pausaComponents = []
        pausaComponents.append(text)
        pausaComponents.append(key_resp_2)
        for thisComponent in pausaComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "pausa"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = pausaClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # underestimates by a little under one frame
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            
            # *key_resp_2* updates
            if t >= 0.0 and key_resp_2.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_resp_2.tStart = t  # underestimates by a little under one frame
                key_resp_2.frameNStart = frameN  # exact frame index
                key_resp_2.status = STARTED
                # keyboard checking is just starting
                key_resp_2.clock.reset()  # now t=0
                event.clearEvents(eventType='keyboard')
            if key_resp_2.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                    key_resp_2.rt = key_resp_2.clock.getTime()
                    # a response ends the routine
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pausaComponents:
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
        
        #-------Ending Routine "pausa"-------
        for thisComponent in pausaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_2.keys in ['', [], None]:  # No response was made
           key_resp_2.keys=None
        # store data for pausa_if (TrialHandler)
        pausa_if.addData('key_resp_2.keys',key_resp_2.keys)
        if key_resp_2.keys != None:  # we had a response
            pausa_if.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.nextEntry()
        
    # completed pauza repeats of 'pausa_if'
    
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    if doleva==1:
        Vsipka='< '
        if bilyvlevo:
            ctverecname = "whitesquare.png"
        else:
            ctverecname = "blacksquare.png"
    else:
        Vsipka=' >'
        if bilyvlevo:
            ctverecname = "blacksquare.png" 
        else:
            ctverecname = "whitesquare.png"
    
    if nahore==1:
        sipkay=0.0
    else:
        sipkay=-0.0
    
    cassum = 60+sipkaframu
    text_sipka.setText(Vsipka)
    text_sipka.setPos([0, sipkay])
    key_resp_sipka = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_sipka.status = NOT_STARTED
    bilyctverec.setImage(ctverecname)
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(ISI)
    trialComponents.append(image_noise)
    trialComponents.append(image_noise_inverse)
    trialComponents.append(text_krizek)
    trialComponents.append(text_sipka)
    trialComponents.append(key_resp_sipka)
    trialComponents.append(bilyctverec)
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
        
        
        
        # *image_noise* updates
        if frameN >= 0 and image_noise.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_noise.tStart = t  # underestimates by a little under one frame
            image_noise.frameNStart = frameN  # exact frame index
            image_noise.setAutoDraw(True)
        elif image_noise.status == STARTED and frameN >= (image_noise.frameNStart + 60):
            image_noise.setAutoDraw(False)
        
        # *image_noise_inverse* updates
        if frameN >= 60 and image_noise_inverse.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_noise_inverse.tStart = t  # underestimates by a little under one frame
            image_noise_inverse.frameNStart = frameN  # exact frame index
            image_noise_inverse.setAutoDraw(True)
        
        # *text_krizek* updates
        if frameN >= 0 and text_krizek.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_krizek.tStart = t  # underestimates by a little under one frame
            text_krizek.frameNStart = frameN  # exact frame index
            text_krizek.setAutoDraw(True)
        elif text_krizek.status == STARTED and frameN >= (text_krizek.frameNStart + 60):
            text_krizek.setAutoDraw(False)
        
        # *text_sipka* updates
        if frameN >= 60 and text_sipka.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_sipka.tStart = t  # underestimates by a little under one frame
            text_sipka.frameNStart = frameN  # exact frame index
            if sipkaframu > 0: #pokud sipka na 0 framu, nebudu ji vubec zobrazovat 
                text_sipka.setAutoDraw(True)

        elif text_sipka.status == STARTED and frameN >= (text_sipka.frameNStart + sipkaframu):
            text_sipka.setAutoDraw(False)
        
        # *key_resp_sipka* updates
        if frameN >= 60 and key_resp_sipka.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_sipka.tStart = t  # underestimates by a little under one frame
            key_resp_sipka.frameNStart = frameN  # exact frame index
            key_resp_sipka.status = STARTED
            # keyboard checking is just starting
            key_resp_sipka.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if key_resp_sipka.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_sipka.keys = theseKeys[-1]  # just the last key pressed
                key_resp_sipka.rt = key_resp_sipka.clock.getTime()
                # was this 'correct'?
                if (key_resp_sipka.keys == str(corrans)) or (key_resp_sipka.keys == corrans):
                    key_resp_sipka.corr = 1
                else:
                    key_resp_sipka.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *bilyctverec* updates
        if frameN >= 59 and bilyctverec.status == NOT_STARTED and sipkaframu<=4:
            # keep track of start time/frame for later
            bilyctverec.tStart = t  # underestimates by a little under one frame
            bilyctverec.frameNStart = frameN  # exact frame index
            bilyctverec.setAutoDraw(True)
        elif bilyctverec.status == STARTED and frameN >= 60: #chci aby predchazel sipku - 17.7.2016
            bilyctverec.setAutoDraw(False)
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
        else:  # this Routine was not non-slip safe so reset non-slip timer
            routineTimer.reset()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # check responses
    if key_resp_sipka.keys in ['', [], None]:  # No response was made
       key_resp_sipka.keys=None
       # was no response the correct answer?!
       if str(corrans).lower() == 'none': key_resp_sipka.corr = 1  # correct non-response
       else: key_resp_sipka.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_sipka.keys',key_resp_sipka.keys)
    trials.addData('key_resp_sipka.corr', key_resp_sipka.corr)
    if key_resp_sipka.keys != None:  # we had a response
        trials.addData('key_resp_sipka.rt', key_resp_sipka.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


win.close()
core.quit()
