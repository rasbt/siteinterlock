# User Guide Overview

This user guide covers the basic usage of the`siteinterlock` package using a re-docking example of based on a protein-ligand crystal complex of monofunctional chorismate mutase and prephenic acid (PDB code: [1com](http://www.rcsb.org/pdb/explore/explore.do?structureId=1com) [[1](#References)]). The files we will be working with in this tutorial are located in the `examples/` subdirectory of the `siteinterlock` package.

The following flowchart highlights a typical workflow of a re-docking study, and this guide assumes that you already completed steps 1-3 and  prepared protein-ligand docking poses using your preferred docking tool, for example, [AutoDock Vina](http://vina.scripps.edu) [[2](#References)]. In the following sections, will work with a small set of 6 exemplary docking poses of 1com, which we generated via SLIDE [[3](#References)]), to illustrate the use of the `siteinterlock` package for near-native binding pose selection (steps 3-6).

<div style="max-width:70%; inline-block; margin:0 auto;">
<img src="/images/flowchart-3.png" alt="SiteInterlock workflow">
</div>


# 1 - Organizing Protein Docking Poses as PDB files

In this section, we will prepare our docking poses for rigidity analysis in [ProFlex](). Please

We recommend you to organize the docking poses for re-scoring in a directory structure similar to the one that is shown in the screenshot below.

![](images/pflex_input_dir_structure.png)

Each docking directory contains one docking pose as input for ProFlex. Each input file should contain the protein structure in PDB file as well as the docked ligand. Please also make sure that yto the respective structures are protonated, which is required by ProFlex. Also, you need to prepare a "ligand-free" structure of the protein, which we labeled `1com_nolig`. If you have further questions about the required file format, please take a look at the "1com" example files, which are located in the `examples/proflex_input/` subdirectory.

# References

- [1] Chook, Y.M, J.V Gray, H Ke, and W.N. Lipscomb. 1994. “The Monofunctional Chorismate Mutase from Bacillus Subtilis. Structure Determination of Chorismate Mutase and Its Complexes with a Transition State Analog and Prephenate, and Implications for the Mechanism of the Enzymatic Reaction.” J.Mol.Biol. 240: 476–500.
- [2] Trott, Oleg, and Arthur J. Olson. 2009. “AutoDock Vina: Improving the Speed and Accuracy of Docking with a New Scoring Function, Efficient Optimization, and Multithreading.” Journal of Computational Chemistry 31 (2). Wiley Subscription Services, Inc., A Wiley Company: NA – NA. doi:10.1002/jcc.21334.
- [3] Zavodszky, M. I., and Leslie A. Kuhn. 2005. “Side-Chain Flexibility in Protein-Ligand Binding: The Minimal Rotation Hypothesis.” Protein Science 14 (4). Cold Spring Harbor Laboratory Press: 1104–14. doi:10.1110/ps.041153605.
