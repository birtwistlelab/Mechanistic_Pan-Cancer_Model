# Mechanistic Pan-Cancer Model #

## Getting Started ##

My name is Mike Saint-Antoine, and I wrote the Python code for the model (translating it from the original Matlab version).
If you have any questions about how the code works, you can reach me at mikest@udel.edu.
If you have any questions about the actual biology of the model, I probably won't be able to answer those since I only translated the code and don't know much about the biology behind it.
But you could try contacting Marc Birtwistle or Mehdi Bouhaddou (the original creator of the Matlab model) with those questions.

## Install instructions

To install with Conda:

1. Create a conda environment called `mpcmodel`:

   ```
   $ conda create -n mpcmodel python=3.6
   ```

2. Activate the environment and install the necessary packages into it:

   ```
   $ source activate mpcmodel
   $ conda install -c conda-forge "blas=*=openblas" numpy scipy pandas matplotlib xlrd
   $ conda install -c conda-forge sundials==3.1 assimulo
   ```

3. Run the test case:

   ```
   $ python test2.py
   ```

## Palmetto Instructions ##

To run this workflow as a PBS script:

1. Create the following PBS script in the project directory (call it `mpcmodel.pbs` or anything you like):

   ```
   #PBS -l select=1:ncpus=4:mem=8gb,walltime=4:00:00

   module load anaconda3/5.1.0

   source activate mpcmodel

   cd $PBS_O_WORKDIR

   python -v

   python test2.py
   ```

2. Submit it by first navigating to the project directory, and then running `qsub`:

   ```
   $ cd /path/to/Mechanistic_Pan-Cancer_Model
   $ qsub mpcmodel.pbs
   ```

## Running Simulations ##

To start running simulations, you only need to run either test.py or test2.py as shown above. Everything else will be called from those files. Of course, you can also make your own file to start running simulations from.
Just make sure to import 'numpy', 'RunPrep', and 'RunModel' at the top.

Let's take a look at an example of a simulation so that I can explain each part......

th=12;
flagD=1;
xoutS = []
xoutG = []
[dataS, dataG] = RunPrep()
STIM = np.zeros(shape = (775));
STIM [84-1] = 0.00385
[t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)
np.savetxt('t\_deterministic.csv', t, delimiter=',')
np.savetxt('xoutG\_deterministic.csv', xoutG, delimiter=',')
np.savetxt('xoutS\_deterministic.csv', xoutS, delimiter=',')




"th=12" means that we're going to simulate 12 hours of time.

"flagD=1" means that this will be a deterministic simulation. If we had put "flagD=0", then it would be a stochastic simulation.



**Important!!!**
"xoutS=[]" and "xoutG=[]" mean that we're passing in blank slates as the xoutS and xoutG variables.
However, we could also pass in xoutS and xoutG values that have been generated in previous simulations.
To do this, just set the values of xoutS and xoutG to the last row from the xoutS and xoutG output from a previous simulation.
So, for example:
[t, xoutG, xoutS] = *first simulation*
xoutS = np.matrix(xoutS[xoutS.shape[0]-1,:])
xoutG = np.matrix(xoutG[xoutG.shape[0]-1,:])
* now xoutS and xoutG are full of the output values from the previous simulation, and ready to be passed into a new simulation *



"[dataS, dataG] = RunPrep()" calls the RunPrep function, which initializes some data that will be passed into the model.

"STIM = np.zeros(shape = (775));" creates the stimuli array that will be passed into the model. We're filling it with zeroes at first, but can add in stimuli as we like.

"STIM [84-1] = 0.00385" adds a stimulus into the stimuli array. The index is set like 84-1 instead of 83 because this model was originally in Matlab, which starts array indices at 1 instead of 0.
However, you could write "STIM [83] = 0.00385" instead and get the same result. But if you're used to using the Matlab model, just keep in mind that you're really talking about the 84th index of the Matlab model, not the 83rd.



"[t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, dataG.kTCleak, dataG.kTCmaxs)" calls the model and passes in the parameters.

**Important!!!**
In this example we're passing in dataG.kTCleak and dataG.kTCmaxs, which are the kTCleak and kTCmaxs generated in RunPrep.
However, we could also choose to pass in empty arrays here, like this:
"[t, xoutG, xoutS] = RunModel(flagD, th, STIM, xoutS, xoutG, dataS, dataG, [], [])"
Then, the kTCleak and kTCmaxs data will be read in from CSVs by the RunModel function.
I'm not sure what the difference is in biological terms between these two options, I just made it this way to be exactly like the Matlab model.



The lines "np.savetxt('t_deterministic.csv', t, delimiter=',')", "np.savetxt('xoutG_deterministic.csv', xoutG, delimiter=',')", "np.savetxt('xoutS_deterministic.csv', xoutS, delimiter=',')" save the output of the model to CSV files, so that they can be accessed later.

## MYSTERIOUS FOR-LOOP BUG ##

There are probably going to be times when you want to run simulations of several different parameter sets several different times in order to generate data from a large sample of cells.
When doing this, it's very important to not have different parameter set simulations being run within the same for-loop. I don't know why. I'm not sure if this is due to a memory allocation issue in Python, or some kind of glitch on my computer.
But when I tried running different simulations inside the same for-loop, the results would sometimes, but not always, come out wrong.



Let me give an example to try to explain what I'm talking about here.

Let's say we have 3 different parameter sets, and we want to run 10 simulations of each.

The intuitive way to write the code might be something like this:



for count in range(10):

  *run simulation with first parameter set*
  *save data to CSVs*

  *run simulation with second parameter set*
  *save data to CSVs*

  *run simulation with third parameter set*
  *save data to CSVs*



^ DON'T DO IT LIKE THIS!! IMPORTANT! Again, I don't know why, but this sometimes leads to the results getting scrambled. Like the output from the second parameter set will get overwritten by the output from the third parameter set, or something weird like that.


It's very important to put each parameter set in its own for-loop, like this:

for count in range(10):
  *run simulation with first parameter set*
  *save data to CSVs*

for count in range(10):
  *run simulation with second parameter set*
  *save data to CSVs*

for count in range(10):
  *run simulation with third parameter set*
  *save data to CSVs*


^ This will produce the correct results, and both ways of writing the code have about the same runtime.

Anyway, it is very important to keep this in mind to avoid problems in the output data.



## Issues/Questions ##


That's all I have for now. Feel free to contact me if you have any questions!
