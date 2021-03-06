# VDJ Recombination


## System Analysis

	- variables

		- concepts
			- relationship type variation (junctional diversity)
			- signal joint
			- functional type (VDJ gene segments, enzyme types, immunoglobulin types)

		- system

			- b/t-cell
			- bone marrow/lymphatic system
			- adaptive immune system

		- components

			- resource: DNA
			- change rule execution objects: enzymes
			- subset types: variable, joining, diversity, & constant gene segments on chains in chromosome loci
			- position: subset type DNA chromosome subsets

		- intents

			- protecting host by attacking pathogens
			- notifying immune system by tagging pathogens

		- processes

			- key processes known to create overall process failure:
				- Artemis hairpin opening process

			- optional processes/inputs
				- resolving discrepancy between number of bases (removing/adding nucleotides)

			- relevant external/subsequent/sub processes
				- somatic recombination inheritance: once a recombination is done, any daughter cells will have same recombinated DNA so the process doesnt have to be applied to every cell generated from recombined DNA cells

			- output processes (mechanism of action)
				- binds to antigen to alert immune system to attack pathogen with that antigen
				- binds to antigen to interfere with pathogen cell activity or survival

		- specific system interfaces

			- communication

				- signaling
					- receptor/antigen-binding region

				- hub
					- DNA-PK is a hub for other proteins & enzymes (artemis, xrcc4, dna ligase iv, cernunnos, & certain DNA polymerases)

				- cooperation
					- protein/enzyme

				- identification
					- RSS recognition by RAG1 enzyme

			- structure

				- layers
					- host system (t-cell, b-cell)
					- system object (cell)
					- host process (cell development)
					- system process (recombination)
					- relationship (position in cell system object)
					- resource to alter (DNA)
					- subset (of resource to be altered, DNA)
					- sequence (of resource to be altered, DNA)
					- units (of resource to be altered & processors - amino acids/nucleotides/bases)
					- processors (enzymes, proteins)
					- limit (validation/protection/regulation) processes (testing, apoptosis)

				- position
					- chromosome position
					- gene segment position
					- enzyme position
					- signal joint position (re-enters the genome to cause changes that are not optimal)

				- component
					- phosphorus is a key component providing an interface to frame the process on
					- DNA
					- amino acid

				- groups
					- base pairs
					- sequences
					- segments
					- DNA-PK recruitment network

				- links
					- DNA-PK binding relationship to DNA ends
					- DNA-PK activation of artemis

				- limits
					- continuity requirement for final protein sequence
					- structural inevitability (1-1 relationship) is injected at various points of the process
					- ratios (5-3, 12:23 rule, 2 heavy :: 2 light, etc)

	- variance injection points
		- target output structure (antigen-binding region or t-cell receptor for a specific pathogen antigen)
		- input components
		- processes
			- legitimate processes
			- illegitimate processes
				- point mutation (can produce slight variation in variable segments of daughter cells)
		- scope
			- specificity of solution
				- immunoglobulin type (class-switching)
		- asymmetry
			- flexibility of variation processes
				- heterodimeric antibodies
					- requires projections & gaps to align small/large amino acids with disulfide bonds

		- intents
		- constants
		- assumptions
		- limits
		- requirements
		- variable metadata (position, application, connection)
		- order of processes
		

	- solution types

		- exporting solution type across context/system types
			- can t-cell solution types be converted to b-cell solution types? if so which functions are required to translate a t-cell solution to a b-cell solution? 

		- adapting system to generate structures

		- process order
			- should tests be applied after potential output is created or earlier in the creation process


	- problem types (rules/types generating failure points)

		- missing requirement

			- missing attributes
				- continuity: DNA does not remain in-frame (continuous segment) 

			- missing types

			- missing objects (groups, limits, connections, information)

			- missing core/system process (copying, nicking, applying enzyme, identifying signal)

		- mismatched requirement (invalidating variation)

			- mismatch in enforcement (rule & variance allowed) 
				- processes not structurally determined to be inevitable (1-1 mapping between structure & process)

			- variation of constants:
				- RSS are supposed to have constant heptamer & nonamer sequences (heptamer: CACAGTG and nonamer: ACAAAAACC)
				- constant gene segments are converted to variable, joining, diversity gene segments in transit/mutation/copying error

			- constants of variables:
				- RSS are supposed to vary in sequence
				- variable, joining, diversity gene segments are converted to a constant in transit/mutation/copying error

			- structure that emerges/enables other functionality is distorted
				- the hydroxyl & phosphate groups are distorted, so the hydroxyl group cant attack the phosphodiester bond of the other strand
				- the chain is distorted
					- a heavy/light/alpha/beta chain doesnt have all the gene segment regions (variable, joining, diversity, constant) it should

			- position is distorted:
				- the hairpin stem-loop is supposed to be on the coding segment
				- a blunt end is supposed to be on the signal segment

			- functionality enabling other functionality is distorted
				- autophosphorylation doesnt occur, so artemis isnt activated and hairpin segment isnt opened

			- functionality that emerges directly from structure is distorted when structure is distorted
				- blunt end/hairpin ends are distorted, so their function is deactivated
				- the replacement of a subset is deactivated if the subset is not made compatible in length or other structural attributes
				- signals are deactivated when information in the signal is distorted

			- intra-type/sub-type variation
				- variation exceeding the limits of a type to create a new type may not be useful for a process with strict limits (creating a new type of immunoglobulin)
				- antibodies are supposed to have heavy & light chains
				- most t-cell receptors are supposed to have alpha & beta chains 
				- antibody proteins are supposed to have antigen-binding regions
				- t-cells are supposed to have receptors
				- the DNA is supposed to have coding/signal segments

			- invalid requirement (assumption)
				- assumption: atp hydrolysis is not necessary
					- atp hydrolysis process fails & creates errors due to lack of enforcement of non-necessity of atp hydrolysis

			- variation in metric/test accuracy (false test result when it should have passed)
				- the test to tell if the generated antibody antigen-binding region or t-cell receptor will attack a host cell fails when it should pass
					- the host cell antigen is faulty
					- the AIRE activation process is faulty
					- the testing process is faulty
					- the similarity to a host cell is irrelevant or wouldnt happen outside the test zone
					- the thymus or bone marrow testing zone is faulty
					- its occurring outside of normal testing zones
					- the antigen was damaged in production or transport to the thymus
					- apoptosis was triggered by another attribute/rule and the antigen was rejected irrelevantly

			- side effect outputs are not destroyed or re-used
				- signal joint is not destroyed & can alter DNA further

		- invalidating condition of process:

			- similarity between swapped components
				- the swap operation is supposed to generate variation
				- similarity between existing & created antibody antigen-binding regions or t-cell receptors (the process is optimal for creating new antibodies/t-cell receptors, so creating the same ones is not an optimal implementation of the process unless there's a deficit of those)

	- emergent attributes

		- affinity 
			- connection potential between key objects (pathogen & immune cell)
				- ability of t-cell receptor or antigen-binding antibody region to bind to antigens



## Variable-diversity-joining (VDJ) recombination process


	- definition
		- process that rearranges variable, joining & diversity gene segments

	- frequency: 
		- occurs only in developing lymphocytes during the early stages of T & B cell maturation

	- inputs

		- components:

			- recombination signal sequences: protected sequences of noncoding DNA recognized by RAG1/2 enzymes during VDJ recombination in B/T cells

				- components of recombination signal sequences:
					- a heptamer of seven conserved nucleotides
					- a spacer region of 12/23 basepairs in length
					- a nonamer of 9 conserved nucleotides

				- Recombination signal sequences allow specific recombinations to be executed, by communicating position of VDJ gene segments
				- VDJ recombination enzymes recognize & bind to recombination signal sequences around the VDJ gene segments

				- RSS vary in sequence but have constant heptamer & nonamer sequences (heptamer: CACAGTG and nonamer: ACAAAAACC)
				- the sequence of the spacer region sequence is often lost
				- the length of the spacer region sequence is rarely lost
				- the spacer region length is usually about 1 or 2 turns of the DNA strand (1 turn = 12 basepairs, 2 turns = 23 basepairs)

				- 12/23 rule: gene segments to be recombined are usually adjacent to Recombination signal sequences of various spacer lengths (one has a "12 RSS" and one has a "23 RSS") 

					- to do: clarify which configuration this rule allows:
						12 RSS - V D J - 23 RSS
						12 RSS - V - 23 RSS
						V - 12 RSS - D J - 23 RSS

			- enzymes & proteins:

				- VDJ recombinase: a diverse collection of enzymes

					- DNA-dependent protein kinase (DNA-PK)
					- X-ray repair cross-complementing protein 4 (XRCC4)
					- DNA ligase IV
					- Cernunnos: non-homologous end-joining factor 1 (NHEJ1), aka XRCC4-like factor [XLF], the Paralog of XRCC4 & XLF (PAXX)
					- DNA polymerases λ & μ

					- enzymes specific to lymphocytes (RAG, TdT)
						- recombination activating genes 1 & 2 (RAG)
						- terminal deoxynucleotidyl transferase (TdT): a template-independent DNA polymerase that adds non-templated (N) nucleotides to the coding end during VDJ recombination, exhibiting a tendency to use G/C nucleotides, though the process of TdT adding nucleotides to the coding end is mostly random
							- like all DNA polymerases, Tdt adds nucleotides to a strand in a 5-3 direction

					- other enzymes found in other cell types or everywhere:
						- Artemis nuclease, a member of the ubiquitous non-homologous end joining (NHEJ) pathway for DNA repair


	- context

		- when building lymphocytes, recombination occurs to generate new variable/diversity/joining gene segments of the antibody's fragment antigen-binding region or the t-cell's receptor, so that new antibodies or t-cell receptors are generated which can handle new antigens

		- occurs in immune/lymphoid systems

			- antibody (specifically immunoglobulin in bone marrow for b cells):

				- composed of heavy & light chains
				- these chains contain constant (C) & variable (V) regions encoded on three antibody DNA loci (heavy, kappa, lambda)
				- fragment antibody-binding (Fab) region: section of an antibody protein that is variable & binds to different antigens

				- heavy chain: large polypeptide subunit of the antibody 
					- defines the antibody isotype (constant gene segments)
					- humans have five heavy chain isotypes
				    - on antibody DNA's chromosome 14's heavy locus (IGH)
				   	- 2 Constant (Cμ & Cδ) gene segments
				   	- 44 Variable (V) gene segments
				   	- 27 Diversity (D) gene segments
				   	- 6 Joining (J) gene segments

				- light chain: small polypeptide subunit of the antibody 
			    	- on antibody DNA's chromosome 2's kappa locus (IGK) & chromosome 22's lambda (λ) locus (IGL)
				   	- 2 Constant (Cλ & Cκ) gene segments 
				   	- Variable & Joining gene segments
				   	- do not have D gene segments
				   	- has protein-coding genes that can be lost during rearrangement

			- t-cell receptors (in thymus for t cells):

				- like antibody genes, most T cell receptor genes contain:
					- beta chains (V, D, & J gene segments)
					- alpha chains (V & J gene segments)


	- related processes

		- somatic recombination
		- ligation process using DNA ligase IV to ligate coding ends once processed
		- XRCC4, cernunnos, & DNA-PK alignment of DNA ends 
		- XRCC4, cernunnos, & DNA-PK recruitment of terminal deoxynucleotidyl transferase (TdT)
		- TdT adding nucleotides to strands in 5-3 direction
		- polymerase adding nucleotides to strands in 5-3 direction
		- DNA-PK autophosphorylation
		- DNA-PK binding to each broken DNA end
		- DNA-PK recruits other proteins including artemis, xrcc4, dna ligase iv, cernunnos, & certain DNA polymerases
		- artemis activation
		- artemis hairpin opening
		- DNA enzyme repair process
			- enzyme nucleotide adjustments for compatibility, in case center of hairpin segment is not opened & sides are unequal
			- creating palindromic nucleotides from off-center opening of hairpin segment
			- exonucleases removing bases from coding ends
			- template-independent TdT adding non-templated nucleotides
		- DNA copying, marking/nicking, identification/recognition, deletion, synthesis, connection, ordering, mutation, activation, transcription, translation, conversion, rearrangement, assembly, expression


	- explanatory interface/variance source

		- DNA rearrangement causes copies of each gene segment type (variable gene segment copy + diversity gene segment copy + joining gene segment copy) to go in any given lymphocyte, generating many possible antibodies 
			- there are around 3×10^11 combinations
			- some combinations are removed due to self reactivity, determined by testing in the thymus against host cell antigens, expressed using the autoimmune regulator protein (AIRE)


	- types

		- system object type connection:
			- a t-cell's receptor is like an antibody's fragment antigen-binding region, both being part of the antibody superfamily
		
		- contextual types:
			- antibodies have heavy & light chains, whereas most t-cell receptors have alpha & beta chains
		
		- input types:
			- each chain has some of the gene segment regions (variable, joining, diversity, constant)
			- VDJ types: variable, joining, & diversity gene segment types influence variable sections of antibody proteins & t-cell receptors
			

	- output:

		- output object
			- general:
				- b cell antibodies/immunoglobulins
				- T cell receptors (TCRs)
			- specific:
				- final product is new amino acid sequences in antigen-binding regions of antibody proteins & t-cell receptors

		- output function
			- these new amino acid sequences enable antibodies & t-cells to recognize antigens (from pathogens, cancerous cells, allergens & healthy host cells)
			
		- output filters
			- validation
				- lymphocytes are tested against host antigens expressed by autoimmune regulatory protein (AIRE) in the thymus
				- lymphocytes that self-react are eliminated with apoptosis to prevent autoimmunity
		
		- output impact
			- variation in resource combination


	- process:

		1. VDJ recombinase (RAG1 enzyme) binds a recombination signal sequence around a VDJ segment
		2. creates a nick on one strand of the DNA between the first base of the Recombination signal sequence just before the heptamer & the coding segment of the RSS
			- ATP hydrolysis (conversion into energy, ADP, AMP, or orthophosphates to enable work) is not necessary bc its energetically neutral
		3. a free 3' hydroxyl group and a 5' phosphate group is formed on the same strand
		4. the recombinase positions the hydroxyl group to attack the phosphodiester bond of the opposite strand
		5. two DNA ends are formed from this attack:
			- the hairpin stem-loop on the coding segment
			- a blunt end on the signal segment
		6. a recombination center executes the DNA nicking & hairpin formation simultaneously
		7. prior to ligation, the blunt signals ends are processed more, leading to junctional diversity (relationship type variation)
			- DNA-PK binds to each broken DNA end
			- DNA-PK recruits other proteins including artemis, xrcc4, dna ligase iv, cernunnos, & certain DNA polymerases
			- DNA-PK forms a complex, leading to its autophosphorylation
			- the autophosphorylation of DNA-PK activates artemis
			- artemis's activity opens the coding end hairpin segments
			- if the coding end hairpin segments are opened at the center, a blunt DNA end will result
			- usually its not at the center and one strand has extra bases
			- when DNA repair enzymes resolve the discrepancy in extra bases, the palindromic sequences produced are the reason why the corrected strand are called palindromic nucleotides
			- the Artemis hairpin opening process is crucial to VDJ recombination success
 				- XRCC4, cernunnos, & DNA-PK align the DNA ends and use terminal deoxynucleotidyl transferase enzyme to add non-templated nucleotides to the coding end
			- exonucleases remove bases from the coding ends, including palidromic (P) or non-templated (N) nucleotides that may have formed
			- DNA polymerases lambda & mu then add nucleotides as needed to make the two ends compatible for joining
			- the process of 1, exonucleolytic removal of bases & P/N nucleotides & 2, adding nucleotides for compatibility, is possible but not enforced
			- the processed coding ends are ligated together using DNA ligase IV

		8. the blunt signal ends are flush-ligated together to form a signal joint (all the interim pieces between coding segments - a circle DNA segment of the intervening sequences between the coding segments)
			- signal joints may re-enter the genome and activate oncogenes or interrupting regulation gene function

		9. this process results in high variability in the antigen-binding region, even with the same gene segments as components, allowing new immunoglobulin antibodies or t-cell receptors to be generated even if the bio system hasnt encountered the corresponding pathogen antigens or a new version of an encountered pathogen before

		- this costly process can only work if the DNA remains in-frame (continuous segment) to maintain the right amino acid sequence in the final protein product - otherwise the cell development will stop & die - so this process has strict limits to succeed


	- sub-process:

		- b-cell process

			- heavy chain

				1. delete DNA between a D & J gene segment (on chromosome 14's heavy chain locus)
				2. add a V gene segment from upstream the DJ combination
				3. delete DNA between V & D segments to form a VDJ segment
				4. generate primary transcript/unspliced RNA, containing the heavy chain VDJ region & both constant chains (V-D-J-Cμ-Cδ)
				5. remove sequence between VDJ & constant gene segments by adding a polyadenylated (poly-A) tail after the Cμ chain to the primary RNA
				6. translation of this mRNA leads to the production of the Ig M heavy chain protein

			- light chain

				- light chain kappa (κ) & lambda (λ) chains rearrange similarly, but light chains dont have a D segment
				1. first join V & J chains to give a VJ complex before adding the constant chain gene during primary transcription
				- translation of the spliced mRNA for either the kappa or lambda chains forms the Ig κ or Ig λ light chain protein

			- the mu Ig μ heavy chain + a light chain forms a membrane bound form of the IgM antibody type expressed on the surface of the immature B cell

		- t-cell (thymocyte) receptors process

			- the T cell receptor (TCR) chains undergo a similar recombination process as for antibodies

				1. first the D-to-J recombination occurs in the TCR beta chain
					- this process can involve either:
						- joining the Dβ1 gene segment to one of six Jβ1 segments
						- joining the Dβ2 gene segment to one of six Jβ2 segments

				2. DJ recombination is followed with Vβ-to-DβJβ rearrangements
				3. all gene segments between the Vβ-Dβ-Jβ gene segments in the newly formed complex are deleted 
				4. the primary transcript is synthesized, incorporating the constant domain gene (Vβ-Dβ-Jβ-Cβ)
				5. mRNA transcription splices out any intervening sequence, allowing translation of the full length protein for the TCR beta chain

			- the rearrangement of the alpha (α) chain of the TCR follows β chain rearrangement, & resembles Ig light chain V-to-J rearrangement
			- the assembly of the beta & alpha chains results in formation of the alpha-beta-TCR that is expressed on a majority of T cells

