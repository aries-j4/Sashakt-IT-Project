(function(){
 
  function buildQuiz(){
   
    const output = [];

   
    myQuestions.forEach(
      (currentQuestion, questionNumber) => {

        
        const answers = [];

       
        for(letter in currentQuestion.answers){

         
          answers.push(
            `<label>
              <input type="radio" name="question${questionNumber}" value="${letter}">
              ${letter} :
              ${currentQuestion.answers[letter]}
            </label>`
          );
        }

        
        output.push(
          `<div class="slide">
            <div class="question"> ${currentQuestion.question} </div>
            <div class="answers"> ${answers.join("")} </div>
          </div>`
        );
      }
    );

    
    quizContainer.innerHTML = output.join('');
  }

  function showResults(){

   
    const answerContainers = quizContainer.querySelectorAll('.answers');

   
    let numCorrect = 0;

    
    myQuestions.forEach( (currentQuestion, questionNumber) => {

      
      const answerContainer = answerContainers[questionNumber];
      const selector = `input[name=question${questionNumber}]:checked`;
      const userAnswer = (answerContainer.querySelector(selector) || {}).value;

      
      if(userAnswer === currentQuestion.correctAnswer){
        
        numCorrect++;

        
        answerContainers[questionNumber].style.color = 'green';
      }
     
      else{
        
        answerContainers[questionNumber].style.color = 'red';
      }
    });

    if(numCorrect > 7)
        {
          resultsContainer.innerHTML = `<div class="ansbox">You scored: ${numCorrect} out of ${myQuestions.length}
                                        <p> Great Job!!!</p></div>`;
        }
        else if(numCorrect > 3)
        {
          resultsContainer.innerHTML = `<div class="ansbox">You scored: ${numCorrect} out of ${myQuestions.length}
                                        <p> Keep Going! You can do much better</p></div>`;
        }
        else
        {
          resultsContainer.innerHTML = `<div class="ansbox">You scored: ${numCorrect} out of ${myQuestions.length}
                                        <p> Need to brush up on some general awareness...eh?</p></div>`;
        }
  }

  function showSlide(n) {
    slides[currentSlide].classList.remove('active-slide');
    slides[n].classList.add('active-slide');
    currentSlide = n;
    if(currentSlide === 0){
      previousButton.style.display = 'none';
    }
    else{
      previousButton.style.display = 'inline-block';
    }
    if(currentSlide === slides.length-1){
      nextButton.style.display = 'none';
      submitButton.style.display = 'inline-block';
    }
    else{
      nextButton.style.display = 'inline-block';
      submitButton.style.display = 'none';
    }
  }

  function showNextSlide() {
    showSlide(currentSlide + 1);
  }

  function showPreviousSlide() {
    showSlide(currentSlide - 1);
  }

  const quizContainer = document.getElementById('quiz');
  const resultsContainer = document.getElementById('results');
  const submitButton = document.getElementById('submit');
  const myQuestions = [
    {
      question: "Approximately what percentage of women worldwide have experienced physical and/or sexual violence?",
      answers: {
        a: "15%",
        b: "35%",
        c: "55%"
      },
      correctAnswer: "b"
    },
    {
      question: "Childhood experiences of violence can be a risk factor to perpetrate and/or experience violence as an adult?",
      answers: {
        a: "True",
        b: "False",
      },
      correctAnswer: "a"
    },
    {
      question: "The International Day for the Elimination of Violence against Women is commemorated yearly on 25 November. What is the historical significance behind this date?",
      answers: {
        a: "It is on this day in 1960 that the Mirabal sisters, political activists in the Dominican Republic, were assassinated.",
        b: "It is on this day in 1994 that many women were massacred during the Rwandan genocide.",
        c: "There is no historical significance! The United Nations randomly picked a day that wasn’t already taken by another International Day.",
      },
      correctAnswer: "a"
    },
    {
      question: "Globally, how prevalent is physical and sexual intimate partner violence and/or sexual violence by a non-partner?",
      answers: {
        a: "1 in 6 women experience this",
        b: "1 in 4 women experience this",
        c: "1 in 3 women experience this",
      },
      correctAnswer: "c"
    },
    {
      question: "Health care providers cannot offer anything for women experiencing violence true/false",
      answers: {
        a: "True",
        b: "False",
      },
      correctAnswer: "b"
    },
    {
      question: "Sometimes it is women’s own fault if they are raped",
      answers: {
        a: "True",
        b: "False",
      },
      correctAnswer: "b"
    },
    {
      question: "The Convention on the Elimination of all forms of Discrimination Against Women(CEDAW), was adopted by the United Nations General Assembly in",
      answers: {
        a: "1981",
        b: "1975",
        c: "1979"
      },
      correctAnswer: "c"
    },
    {
      question: "The Declaration on the Elimination of Violence Against Women was made by the United Nations General Assembly in",
      answers: {
        a: "1981",
        b: "1993",
        c: "1979"
      },
      correctAnswer: "b"
    },
    {
      question: "Can any person with information about a sexual harassment incident file a complaint to the Complaints Committee?",
      answers: {
        a: "Yes, only with written consent of the complainant",
        b: "Yes, even without written consent of the complainant",
        c: "No"
      },
      correctAnswer: "a"
    },
    {
      question: "Does the Criminal Law (Amendment) Act 2013 recognize stalking as a criminal act?",
      answers: {
        a: "Yes",
        b: "No"
      },
      correctAnswer: "a"
    }
  ];


  buildQuiz();

  const previousButton = document.getElementById("previous");
  const nextButton = document.getElementById("next");
  const slides = document.querySelectorAll(".slide");
  let currentSlide = 0;

  showSlide(currentSlide);

  submitButton.addEventListener('click', showResults);
  previousButton.addEventListener("click", showPreviousSlide);
  nextButton.addEventListener("click", showNextSlide);
})();