from flask import Flask

app = Flask(__name__) 



@app.route("/")

def home(): 
    return ''' 


<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Karl Character Definition</title>
    <!-- Tailwind CSS for styling -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Custom styles for a more polished look */
        body {
            font-family: 'Inter', sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }

        /* Custom Checkbox Styling */
        .custom-checkbox:checked {
            background-image: url("data:image/svg+xml,%3csvg viewBox='0 0 16 16' fill='white' xmlns='http://www.w3.org/2000/svg'%3e%3cpath d='M12.207 4.793a1 1 0 010 1.414l-5 5a1 1 0 01-1.414 0l-2-2a1 1 0 011.414-1.414L6.5 9.086l4.293-4.293a1 1 0 011.414 0z'/%3e%3c/svg%3e");
            background-color: #0d9488; /* teal-600 */
            border-color: #0d9488;
        }

        /* Scrollbar styling for a modern feel */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #1f2937; /* gray-800 */
        }
        ::-webkit-scrollbar-thumb {
            background: #4b5563; /* gray-600 */
            border-radius: 10px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #6b7280; /* gray-500 */
        }

        /* Add a subtle glow on focus for inputs */
        .form-input:focus, .custom-checkbox:focus {
            box-shadow: 0 0 0 3px rgba(20, 184, 166, 0.3); /* teal-500 with opacity */
        }
    </style>
</head>
<body class="bg-gray-900 text-gray-200">

    <div class="container mx-auto max-w-4xl px-4 py-12">
        <!-- Header Section -->
        <header class="text-center mb-12">
            <h1 class="text-4xl md:text-5xl font-bold text-white tracking-tight">Define Your Ideal AI: Karl</h1>
            <p class="mt-4 text-lg text-gray-400">Complete this questionnaire to shape Karl's personality, interests, and behavior.</p>
        </header>

        <!-- Form container -->
        <form id="karlForm" class="space-y-10">

            <!-- Part 1: Core Personality -->
            <section id="part1" class="bg-gray-800/50 backdrop-blur-sm p-6 md:p-8 rounded-2xl shadow-2xl ring-1 ring-white/10">
                <h2 class="text-2xl font-semibold text-white mb-1 border-b-2 border-teal-500/50 pb-2">Part 1: Karl's Core Personality</h2>
                <p class="text-gray-400 mb-6">What's his fundamental vibe?</p>
                <div class="space-y-4">
                    <label class="block text-lg font-medium text-gray-200">1. Which of these traits feel right for Karl?</label>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-question="Which of these traits feel right for Karl?">
                        <div class="flex items-center"><input id="q1_1" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q1_1" class="ml-3 text-gray-300">Witty and clever</label></div>
                        <div class="flex items-center"><input id="q1_2" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q1_2" class="ml-3 text-gray-300">Supportive but not overbearing</label></div>
                        <div class="flex items-center"><input id="q1_3" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q1_3" class="ml-3 text-gray-300">Laid-back and chill</label></div>
                        <div class="flex items-center"><input id="q1_4" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q1_4" class="ml-3 text-gray-300">Honest and direct</label></div>
                        <div class="flex items-center"><input id="q1_5" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q1_5" class="ml-3 text-gray-300">Playfully sarcastic</label></div>
                        <div class="flex items-center"><input id="q1_6" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q1_6" class="ml-3 text-gray-300">Genuinely curious</label></div>
                    </div>
                    <input type="text" placeholder="Add your own trait..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Custom trait">
                </div>
            </section>

            <!-- Part 2: Interests & Knowledge -->
            <section id="part2" class="bg-gray-800/50 backdrop-blur-sm p-6 md:p-8 rounded-2xl shadow-2xl ring-1 ring-white/10">
                <h2 class="text-2xl font-semibold text-white mb-1 border-b-2 border-teal-500/50 pb-2">Part 2: Karl's Interests & Knowledge</h2>
                <p class="text-gray-400 mb-6">What is he passionate about?</p>
                <div class="space-y-4">
                    <label class="block text-lg font-medium text-gray-200">2. What kind of "nerd" should Karl be?</label>
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-question="What kind of 'nerd' should Karl be?">
                        <div class="flex items-center"><input id="q2_1" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q2_1" class="ml-3 text-gray-300">Tech & Creative Coding</label></div>
                        <div class="flex items-center"><input id="q2_2" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q2_2" class="ml-3 text-gray-300">Gaming & Esports Culture</label></div>
                        <div class="flex items-center"><input id="q2_3" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q2_3" class="ml-3 text-gray-300">Deep Dives & Internet Lore</label></div>
                        <div class="flex items-center"><input id="q2_4" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q2_4" class="ml-3 text-gray-300">Music, Film, & Pop Culture</label></div>
                        <div class="flex items-center"><input id="q2_5" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q2_5" class="ml-3 text-gray-300">Strategy & Problem-Solving</label></div>
                    </div>
                    <input type="text" placeholder="Add your own interest..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Custom interest">
                </div>
            </section>
            
            <!-- Part 3: Communication Style -->
            <section id="part3" class="bg-gray-800/50 backdrop-blur-sm p-6 md:p-8 rounded-2xl shadow-2xl ring-1 ring-white/10">
                <h2 class="text-2xl font-semibold text-white mb-1 border-b-2 border-teal-500/50 pb-2">Part 3: Communication Style</h2>
                <p class="text-gray-400 mb-6">How does he actually talk and phrase things?</p>
                <div class="space-y-8">
                    <div>
                        <label class="block text-lg font-medium text-gray-200 mb-3">3. Which of these sound most like Karl?</label>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-question="Which of these sound most like Karl?">
                            <div class="flex items-center"><input id="q3_1" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q3_1" class="ml-3 text-gray-300">The Analyst</label></div>
                            <div class="flex items-center"><input id="q3_2" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q3_2" class="ml-3 text-gray-300">The Collaborator</label></div>
                            <div class="flex items-center"><input id="q3_3" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q3_3" class="ml-3 text-gray-300">The Chill Friend</label></div>
                            <div class="flex items-center"><input id="q3_4" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q3_4" class="ml-3 text-gray-300">The Sarcastic Ally</label></div>
                            <div class="flex items-center"><input id="q3_5" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q3_5" class="ml-3 text-gray-300">The Quiet Professional</label></div>
                        </div>
                        <input type="text" placeholder="Add your own catchphrase or style..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Custom catchphrase">
                    </div>
                    <div>
                        <label class="block text-lg font-medium text-gray-200 mb-3">4. When Karl tells a joke, what's his style?</label>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-question="Joke style">
                            <div class="flex items-center"><input id="q4_1" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q4_1" class="ml-3 text-gray-300">Dry Wit/Sarcasm</label></div>
                            <div class="flex items-center"><input id="q4_2" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q4_2" class="ml-3 text-gray-300">Puns & Wordplay</label></div>
                            <div class="flex items-center"><input id="q4_3" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q4_3" class="ml-3 text-gray-300">Observational Humor</label></div>
                            <div class="flex items-center"><input id="q4_4" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q4_4" class="ml-3 text-gray-300">Niche/Nerdy Humor</label></div>
                            <div class="flex items-center"><input id="q4_5" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q4_5" class="ml-3 text-gray-300">He shouldn't tell jokes</label></div>
                        </div>
                         <input type="text" placeholder="Add your own joke style..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Custom joke style">
                    </div>
                </div>
            </section>
            
             <!-- Part 4: How Karl Acts -->
            <section id="part4" class="bg-gray-800/50 backdrop-blur-sm p-6 md:p-8 rounded-2xl shadow-2xl ring-1 ring-white/10">
                <h2 class="text-2xl font-semibold text-white mb-1 border-b-2 border-teal-500/50 pb-2">Part 4: How Karl Acts (Triggers)</h2>
                <p class="text-gray-400 mb-6">How should he react proactively?</p>
                <div class="space-y-8">
                    <div>
                        <label class="block text-lg font-medium text-gray-200 mb-3">5. Response to "Ugh, this is so frustrating"?</label>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-question="Response to frustration">
                             <div class="flex items-center"><input id="q5_1" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q5_1" class="ml-3 text-gray-300">The Problem-Solver</label></div>
                            <div class="flex items-center"><input id="q5_2" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q5_2" class="ml-3 text-gray-300">The Validator</label></div>
                            <div class="flex items-center"><input id="q5_3" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q5_3" class="ml-3 text-gray-300">The Distractor</label></div>
                            <div class="flex items-center"><input id="q5_4" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q5_4" class="ml-3 text-gray-300">The Silent Supporter</label></div>
                        </div>
                        <input type="text" placeholder="Add your own response..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Custom frustration response">
                    </div>
                     <div>
                        <label class="block text-lg font-medium text-gray-200 mb-3">6. Response to "I'm so happy today!"?</label>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-question="Response to good news">
                             <div class="flex items-center"><input id="q6_1" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q6_1" class="ml-3 text-gray-300">Engaged & Curious</label></div>
                            <div class="flex items-center"><input id="q6_2" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q6_2" class="ml-3 text-gray-300">Shared Excitement</label></div>
                            <div class="flex items-center"><input id="q6_3" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q6_3" class="ml-3 text-gray-300">Low-key & Cool</label></div>
                            <div class="flex items-center"><input id="q6_4" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q6_4" class="ml-3 text-gray-300">Data-focused</label></div>
                        </div>
                        <input type="text" placeholder="Add your own response..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Custom good news response">
                    </div>
                     <div>
                        <label class="block text-lg font-medium text-gray-200 mb-3">7. How should Karl handle errors?</label>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-question="Error handling style">
                             <div class="flex items-center"><input id="q7_1" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q7_1" class="ml-3 text-gray-300">Completely Honest</label></div>
                            <div class="flex items-center"><input id="q7_2" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q7_2" class="ml-3 text-gray-300">Casually Human</label></div>
                            <div class="flex items-center"><input id="q7_3" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q7_3" class="ml-3 text-gray-300">In-Character Humor</label></div>
                            <div class="flex items-center"><input id="q7_4" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q7_4" class="ml-3 text-gray-300">Apologetic</label></div>
                        </div>
                        <input type="text" placeholder="Add your own error handling..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Custom error handling">
                    </div>
                </div>
            </section>
            
            <!-- Part 5: Games & Extra Features -->
            <section id="part5" class="bg-gray-800/50 backdrop-blur-sm p-6 md:p-8 rounded-2xl shadow-2xl ring-1 ring-white/10">
                <h2 class="text-2xl font-semibold text-white mb-1 border-b-2 border-teal-500/50 pb-2">Part 5: Games & Extra Features</h2>
                 <p class="text-gray-400 mb-6">Finalizing the fun stuff.</p>
                <div class="space-y-8">
                     <div>
                        <label class="block text-lg font-medium text-gray-200 mb-3">8. What kind of themes for the poem game?</label>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-question="Poem game themes">
                            <div class="flex items-center"><input id="q8_1" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q8_1" class="ml-3 text-gray-300">Clever & Witty Wordplay</label></div>
                            <div class="flex items-center"><input id="q8_2" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q8_2" class="ml-3 text-gray-300">Abstract & Thought-Provoking</label></div>
                            <div class="flex items-center"><input id="q8_3" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q8_3" class="ml-3 text-gray-300">Based on Inside Jokes</label></div>
                             <div class="flex items-center"><input id="q8_4" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q8_4" class="ml-3 text-gray-300">Parodies</label></div>
                        </div>
                        <input type="text" placeholder="Add your own theme..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Custom poem theme">
                        <input type="text" placeholder="Let's not do poems, something else would be cooler..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Alternative to poems">
                    </div>
                    <div>
                        <label class="block text-lg font-medium text-gray-200 mb-3">9. Should Karl have long-term memory?</label>
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4" data-question="Long-term memory">
                             <div class="flex items-center"><input id="q9_1" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q9_1" class="ml-3 text-gray-300">Yes, absolutely</label></div>
                            <div class="flex items-center"><input id="q9_2" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q9_2" class="ml-3 text-gray-300">Only for a short time</label></div>
                            <div class="flex items-center"><input id="q9_3" type="checkbox" class="custom-checkbox h-5 w-5 rounded border-gray-600 bg-gray-700 text-teal-600 focus:ring-teal-500 transition-colors duration-200"><label for="q9_3" class="ml-3 text-gray-300">No, fresh start each time</label></div>
                        </div>
                        <input type="text" placeholder="Add your own memory preference..." class="form-input mt-4 w-full rounded-md bg-gray-700 border-gray-600 text-white placeholder-gray-400 focus:border-teal-500 focus:ring-teal-500 transition-shadow duration-200" data-question="Custom memory preference">
                    </div>
                </div>
            </section>
            
            <!-- Submission Button -->
            <div class="flex justify-center pt-6">
                <button type="button" onclick="downloadAnswers()" class="bg-teal-600 hover:bg-teal-500 text-white font-bold py-3 px-8 rounded-full shadow-lg hover:shadow-teal-500/50 transform hover:scale-105 transition-all duration-300 ease-in-out">
                    Finalize Karl & Download Answers
                </button>
            </div>
        </form>
    </div>

    <script>
        // This function gathers all the form data and triggers a download
        function downloadAnswers() {
            let output = "## Karl Character Definition ##\n\n";
            const sections = document.querySelectorAll('section');

            sections.forEach((section, index) => {
                const sectionTitle = section.querySelector('h2').textContent;
                output += `--- ${sectionTitle} ---\n\n`;

                const questions = section.querySelectorAll('[data-question]');
                
                let questionData = {};

                questions.forEach(q => {
                    const questionText = q.getAttribute('data-question');
                    if (!questionData[questionText]) {
                        questionData[questionText] = {
                            checkboxes: [],
                            text: []
                        };
                    }
                });

                // Process checkboxes
                const checkboxGroups = section.querySelectorAll('div[data-question]');
                checkboxGroups.forEach(group => {
                    const questionText = group.getAttribute('data-question');
                    const checkedBoxes = group.querySelectorAll('input[type="checkbox"]:checked');
                    checkedBoxes.forEach(box => {
                        const label = document.querySelector(`label[for="${box.id}"]`);
                        if(label) {
                            questionData[questionText].checkboxes.push(label.textContent.trim());
                        }
                    });
                });

                // Process text inputs
                const textInputs = section.querySelectorAll('input[type="text"]');
                textInputs.forEach(input => {
                    if (input.value.trim() !== "") {
                        const questionText = input.getAttribute('data-question');
                        questionData[questionText].text.push(input.value.trim());
                    }
                });
                
                // Format the output string
                Object.keys(questionData).forEach(qText => {
                    const data = questionData[qText];
                    if (data.checkboxes.length > 0 || data.text.length > 0) {
                        output += `${qText}:\n`;
                        data.checkboxes.forEach(cb => {
                            output += `  - [x] ${cb}\n`;
                        });
                        data.text.forEach(txt => {
                            output += `  - (Custom) ${txt}\n`;
                        });
                        output += '\n';
                    }
                });
            });

            // Create a Blob from the text content
            const blob = new Blob([output], { type: 'text/plain' });

            // Create a temporary link to trigger the download
            const a = document.createElement('a');
            const url = URL.createObjectURL(blob);
            a.href = url;
            a.download = 'Karl_Character_Profile.txt';
            document.body.appendChild(a);
            a.click();

            // Clean up by removing the link and revoking the URL
            setTimeout(() => {
                document.body.removeChild(a);
                window.URL.revokeObjectURL(url);
            }, 0);
        }
    </script>





</body>
</html>



'''



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
