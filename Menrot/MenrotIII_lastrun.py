#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.79.01), srpen 19, 2014, at 12:58
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

# Store info about the experiment session
expName = 'AEdist'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Setup filename for saving
filename = u'data' + os.path.sep + '%s_%s' %(expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'D:\\prace\\programovani\\psychopy\\Menrot\\MenrotIII.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=1, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "napoveda"
napovedaClock = core.Clock()
#inicializace na zacatku
textNapoveda=u'ahoj'
text = visual.TextStim(win=win, ori=0, name='text',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)
text2 = visual.TextStim(win=win, ori=0, name='text2',
    text=u'Zm\xe1\u010dkn\u011bte \u0161ipku doprava pro pokra\u010dov\xe1n\xed',    font='Arial',
    pos=[0, -0.5], height=0.05, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0)
text3 = visual.TextStim(win=win, ori=0, name='text3',
    text='default text',    font='Arial',
    pos=[0, -0.6], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "precross"
precrossClock = core.Clock()
text_precross = visual.TextStim(win=win, ori=0, name='text_precross',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "trial"
trialClock = core.Clock()
image = visual.ImageStim(win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=None,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=False, depth=0.0)
ISI = core.StaticPeriod(win=win, screenHz=expInfo['frameRate'], name='ISI')
test_cross = visual.TextStim(win=win, ori=0, name='test_cross',
    text='+',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#inicializace promenne
msqFeedback = ''
textFeedBack = visual.TextStim(win=win, ori=0, name='textFeedBack',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=u'D:\\prace\\programovani\\psychopy\\Menrot\\MenrotIII.psyexp',
    trialList=data.importConditions('menrotIIIconditions.csv'),
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
    loopPauza = data.TrialHandler(nReps=pauza, method='random', 
        extraInfo=expInfo, originPath=u'D:\\prace\\programovani\\psychopy\\Menrot\\MenrotIII.psyexp',
        trialList=[None],
        seed=None, name='loopPauza')
    thisExp.addLoop(loopPauza)  # add the loop to the experiment
    thisLoopPauza = loopPauza.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisLoopPauza.rgb)
    if thisLoopPauza != None:
        for paramName in thisLoopPauza.keys():
            exec(paramName + '= thisLoopPauza.' + paramName)
    
    for thisLoopPauza in loopPauza:
        currentLoop = loopPauza
        # abbreviate parameter names if possible (e.g. rgb = thisLoopPauza.rgb)
        if thisLoopPauza != None:
            for paramName in thisLoopPauza.keys():
                exec(paramName + '= thisLoopPauza.' + paramName)
        
        #------Prepare to start Routine "napoveda"-------
        t = 0
        napovedaClock.reset()  # clock 
        frameN = -1
        # update component parameters for each repeat
        if podle=='vy':
            if verze=='2D':
                textNapoveda = u'shora, od Vás'
            else:
                textNapoveda = u'z boku, od Vás'
        else:
            if verze=='2D':
                textNapoveda = u'shora, od Značky'
            else:
                textNapoveda = u'z boku, od Značky'
        
        text.setText(textNapoveda
)
        text3.setText(opakovani)
        respNapoveda = event.BuilderKeyResponse()  # create an object of type KeyResponse
        respNapoveda.status = NOT_STARTED
        # keep track of which components have finished
        napovedaComponents = []
        napovedaComponents.append(text)
        napovedaComponents.append(text2)
        napovedaComponents.append(text3)
        napovedaComponents.append(respNapoveda)
        for thisComponent in napovedaComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "napoveda"-------
        continueRoutine = True
        while continueRoutine:
            # get current time
            t = napovedaClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *text* updates
            if t >= 0.5 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t  # underestimates by a little under one frame
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            
            # *text2* updates
            if t >= 0.5 and text2.status == NOT_STARTED:
                # keep track of start time/frame for later
                text2.tStart = t  # underestimates by a little under one frame
                text2.frameNStart = frameN  # exact frame index
                text2.setAutoDraw(True)
            
            # *text3* updates
            if t >= 0.5 and text3.status == NOT_STARTED:
                # keep track of start time/frame for later
                text3.tStart = t  # underestimates by a little under one frame
                text3.frameNStart = frameN  # exact frame index
                text3.setAutoDraw(True)
            
            # *respNapoveda* updates
            if t >= 0.5 and respNapoveda.status == NOT_STARTED:
                # keep track of start time/frame for later
                respNapoveda.tStart = t  # underestimates by a little under one frame
                respNapoveda.frameNStart = frameN  # exact frame index
                respNapoveda.status = STARTED
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
                    continueRoutine = False
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in napovedaComponents:
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
        
        #-------Ending Routine "napoveda"-------
        for thisComponent in napovedaComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # check responses
        if respNapoveda.keys in ['', [], None]:  # No response was made
           respNapoveda.keys=None
        # store data for loopPauza (TrialHandler)
        loopPauza.addData('respNapoveda.keys',respNapoveda.keys)
        if respNapoveda.keys != None:  # we had a response
            loopPauza.addData('respNapoveda.rt', respNapoveda.rt)
        
        #------Prepare to start Routine "precross"-------
        t = 0
        precrossClock.reset()  # clock 
        frameN = -1
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        # keep track of which components have finished
        precrossComponents = []
        precrossComponents.append(text_precross)
        for thisComponent in precrossComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "precross"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = precrossClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_precross* updates
            if t >= 0.0 and text_precross.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_precross.tStart = t  # underestimates by a little under one frame
                text_precross.frameNStart = frameN  # exact frame index
                text_precross.setAutoDraw(True)
            elif text_precross.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
                text_precross.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in precrossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "precross"-------
        for thisComponent in precrossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.nextEntry()
        
    # completed pauza repeats of 'loopPauza'
    
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    image.setImage('imagesR/'+obrazek)
    odpoved = event.BuilderKeyResponse()  # create an object of type KeyResponse
    odpoved.status = NOT_STARTED
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(image)
    trialComponents.append(ISI)
    trialComponents.append(odpoved)
    trialComponents.append(test_cross)
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
        if t >= 0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # underestimates by a little under one frame
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
        elif image.status == STARTED and t >= (0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
            image.setAutoDraw(False)
        
        # *odpoved* updates
        if t >= 0 and odpoved.status == NOT_STARTED:
            # keep track of start time/frame for later
            odpoved.tStart = t  # underestimates by a little under one frame
            odpoved.frameNStart = frameN  # exact frame index
            odpoved.status = STARTED
            # keyboard checking is just starting
            odpoved.clock.reset()  # now t=0
            event.clearEvents(eventType='keyboard')
        if odpoved.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
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
        
        # *test_cross* updates
        if t >= 2 and test_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            test_cross.tStart = t  # underestimates by a little under one frame
            test_cross.frameNStart = frameN  # exact frame index
            test_cross.setAutoDraw(True)
        elif test_cross.status == STARTED and t >= (2 + (1.5-win.monitorFramePeriod*0.75)): #most of one frame period left
            test_cross.setAutoDraw(False)
        # *ISI* period
        if t >= 0.0 and ISI.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISI.tStart = t  # underestimates by a little under one frame
            ISI.frameNStart = frameN  # exact frame index
            ISI.start(0.3)
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
    
    # set up handler to look after randomisation of conditions etc
    loopFeedback = data.TrialHandler(nReps=zpetnavazba, method='random', 
        extraInfo=expInfo, originPath=u'D:\\prace\\programovani\\psychopy\\Menrot\\MenrotIII.psyexp',
        trialList=[None],
        seed=None, name='loopFeedback')
    thisExp.addLoop(loopFeedback)  # add the loop to the experiment
    thisLoopFeedback = loopFeedback.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb=thisLoopFeedback.rgb)
    if thisLoopFeedback != None:
        for paramName in thisLoopFeedback.keys():
            exec(paramName + '= thisLoopFeedback.' + paramName)
    
    for thisLoopFeedback in loopFeedback:
        currentLoop = loopFeedback
        # abbreviate parameter names if possible (e.g. rgb = thisLoopFeedback.rgb)
        if thisLoopFeedback != None:
            for paramName in thisLoopFeedback.keys():
                exec(paramName + '= thisLoopFeedback.' + paramName)
        
        #------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock 
        frameN = -1
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        if odpoved.corr:#stored on last run routine
          msqFeedback=u'Správně'
        else:
          msqFeedback=u'Špatně'
        textFeedBack.setText(msqFeedback)
        # keep track of which components have finished
        feedbackComponents = []
        feedbackComponents.append(textFeedBack)
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        #-------Start Routine "feedback"-------
        continueRoutine = True
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            
            # *textFeedBack* updates
            if t >= 0.0 and textFeedBack.status == NOT_STARTED:
                # keep track of start time/frame for later
                textFeedBack.tStart = t  # underestimates by a little under one frame
                textFeedBack.frameNStart = frameN  # exact frame index
                textFeedBack.setAutoDraw(True)
            elif textFeedBack.status == STARTED and t >= (0.0 + (2-win.monitorFramePeriod*0.75)): #most of one frame period left
                textFeedBack.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineTimer.reset()  # if we abort early the non-slip timer needs reset
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        #-------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        thisExp.nextEntry()
        
    # completed zpetnavazba repeats of 'loopFeedback'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'



win.close()
core.quit()
