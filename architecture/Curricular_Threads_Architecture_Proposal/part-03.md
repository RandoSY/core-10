 Preparing a solution                                   Concentration becomes materially meaningful when the learner
                                                        actually measures and mixes.
 Simple circuit & sensor                                Connections, polarity, grounding, intermittent faults, and real
                                                        signals are educationally valuable.
 Motion / robot work                                    Friction, inertia, terrain, mechanical losses, and battery behavior
                                                        create irreducible reality.



    A good target is not “no hardware.” A good target is “the minimum physical contact
    needed to make the virtual and AI layers trustworthy and meaningful.”

A practical access model
 Access level                                           What the learner can do
 Browser only                                           Learn concepts, operate simulations, analyze authentic
                                                        datasets, solve energy-management scenarios, interact with AI.
 Browser + borrowed/shared kit                          Perform occasional canonical anchor experiments and upload
                                                        the record.
 Personal low-cost kit                                  Run canonical experiments locally; reuse the same hardware
                                                        across multiple curricular threads.
 Networked SDL laboratory                               Let AI inspect device capabilities, modify acquisition or
                                                        procedure, and support adaptive experimentation.


This access ladder is important for longevity: the curriculum remains useful even if a learner never owns the
hardware, but hardware adds reality rather than unlocking the curriculum itself.




                                                      10
                                                                                    CURRICULAR THREADS ARCHITECTURE




7. AI and the Adaptive Laboratory
     The long-lived asset is not a fixed app. It is a machine-readable curriculum plus
     machine-readable experimental capability that future AI systems can interpret and
     operate.

What AI should be allowed to do
 AI role                                                Desired behavior
 Tutor                                                  Explain concepts at the learner’s level without weakening the
                                                        physical model.
 Planner                                                Choose or adapt an experiment to the available apparatus and
                                                        the question being asked.
 Instrument collaborator                                Discover sensors / actuators and understand their capabilities
                                                        and limits.
 Data analyst                                           Graph, compare, fit, summarize, and detect anomalies in
                                                        experiment records.
 Critic                                                 Ask whether the experiment actually tests the proposition and
                                                        whether the reasoning is fallacious.
 Safety / constraint checker                            Respect temperature, voltage, chemistry, battery, and
                                                        physiological limits defined by the curriculum.
 Scenario manager                                       Turn finite-energy situations into changing, consequential
                                                        decisions.
 Archivist                                              Preserve the learner’s experiment record and reconnect later
                                                        activities to earlier evidence.



The experiment as a machine-readable object
For longevity, each experiment should be describable independently of a specific app or board. A future AI
should be able to read a compact experiment definition and know what the learner is trying to establish, what
variables matter, which instruments are acceptable, what safety limits apply, what constitutes useful
evidence, and which later curricular activities depend on the result.
 Field                                                  Example content
 Question                                               How much electrical energy becomes useful thermal energy
                                                        when heating 250 g of water?
 Required observables                                   Mass, initial/final temperature, time, electrical Wh.
 Acceptable instruments                                 Scale, temperature sensor, plug-in energy meter or equivalent
                                                        SDL device.
 Safety constraints                                     Container, temperature, electrical isolation, handling limits.
 Expected reasoning                                     Q = mcΔT; compare useful thermal energy with measured input.
 Reusable outputs                                       Raw data, calculated efficiency, uncertainty, energy cost.
 Downstream use                                         NIF energy accounting; Personal Energy load scheduling.



     If experiments are stored this way, the web interface, the low-cost kit, and the AI
     model can all change over time without destroying the curriculum.




                                                     11
                                                                                  CURRICULAR THREADS ARCHITECTURE




8. Preservation and Longevity Strategy
The durability of this work depends less on any single board or application than on separating the enduring
intellectual content from the replaceable implementation layers.
 Preserve as enduring assets                            Allow to evolve
 Curricular hierarchy and ownership rules               Specific microcontroller boards
 Canonical experiment definitions                       Specific sensors and vendors
 Scientific models and required concepts                Transport: USB, BLE, Wi-Fi, MQTT, etc.
 Safety constraints and valid operating ranges          Dashboard frameworks and UI design
 Reusable datasets and experiment records               AI model or provider
 Machine-readable device capability descriptions        Programming language / runtime
 Scenario libraries and synthesis problems              Hosting platform
 Plain-language learner explanations                    Packaging and branding



Design principles for the web archive
 • Open, ordinary file formats wherever practical: CSV/JSON for data, Markdown/HTML for text, images for
   diagrams, simple schemas for experiment definitions.
 • Every physical experiment should have a browser-usable counterpart using authentic preserved data.
 • Every web simulation should disclose which parts are modeled and which parts come from measurement.
 • Hardware should enhance the course rather than gate access to it.
 • Device capability descriptions should be human-readable as well as AI-readable.
 • The same experiment should be runnable with multiple hardware implementations whenever feasible.
 • AI should be replaceable: the curriculum must not depend on one proprietary model understanding hidden
    conventions.
 • Preserve the learner’s evidence and reasoning, not only a final answer.
    Longevity comes from forcing as much of the intellectual system as possible upward
    into portable descriptions, datasets, and web experiences - while keeping enough
    physical reality underneath to prevent the curriculum from becoming detached from
    the world it is meant to explain.




                                                     12
                                                                                  CURRICULAR THREADS ARCHITECTURE




9. Recommended First Implementation
   Build the smallest complete version that demonstrates the architecture end to end.

Phase 1 - define and tag
• Inventory every existing activity in CORE 10, Kitchen Inquiry, One Cup Chemistry, and NIF.
• Tag each activity CANONICAL, REVISIT, SYNTHESIS, or REDUNDANT.
• Assign one primary curricular owner to every canonical experiment.
• For every revisit, write one sentence stating what new capability it adds.
• Merge or remove any duplicate that cannot answer that question.

Phase 2 - create the web twin
• For each canonical experiment, preserve one exemplary authentic dataset plus metadata and uncertainty.
• Create a browser page that can explain the experiment, display the data, and let the learner manipulate or
  re-analyze it.
• Add an AI interaction layer that can ask questions, critique conclusions, and adapt follow-up tasks.
• Make the physical-hardware path optional where possible and explicit where necessary.

Phase 3 - demonstrate synthesis
• Build one Personal Energy Laboratory scenario using previously generated experiment records.
• Require the learner to allocate finite solar generation and battery reserve among heat, refrigeration, water
  heating, and transportation.
• Let AI adapt the scenario in response to the learner’s decisions and explain the consequences using
   earlier evidence.
• Include at least one deliberate fault or conceptual trap so the system must question the premise rather
   than merely calculate.

Suggested first web demonstration
Component                                               Minimal implementation
Physical anchor                                         One low-cost temperature or energy-measurement experiment
                                                        using Uno/MFS or equivalent.
Persisted record                                        Browser-readable CSV/JSON + experiment metadata.
Web experience                                          Graphing, parameter changes, comparison with reference
                                                        datasets.
AI role                                                 Explain, critique, ask for missing evidence, and propose a better
                                                        measurement if needed.
Synthesis                                               Use the measured load in a small solar/battery household
                                                        budget.



   This single loop would demonstrate the entire philosophy: physical reality →
   preserved evidence → web reasoning → AI adaptation → practical decision.



                                                      13
                                                                          CURRICULAR THREADS ARCHITECTURE




10. The Proposal in One Page
Design question                                 Answer
What is the root?                               CORE 10: common scientific literacy and experimental
                                                reasoning.
What are the three primary branches?            Kitchen Inquiry Lab, One Cup Chemistry, and NOTHING IS
                                                FREE.
How is duplication controlled?                  Every activity is CANONICAL, REVISIT, or SYNTHESIS;
                                                redundant copies are removed.
Where does biology live?                        Across the curriculum as the living-system context the physical
                                                world must support.
Where does SDL live?                            Across the curriculum as sensing, logging, preservation,
                                                experimentation, and AI-facing infrastructure.
What is the capstone?                           Personal Energy Laboratory: informed administration of life
