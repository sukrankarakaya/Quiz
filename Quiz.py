class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    def displayQuestion(self):
        question = self.getQuestion()
        print(f'soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+ q)
        answer =input('Cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1
    def loadQuestion(self):
        if len(self.questions)== self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print("100 ÜSTÜNDEN PUANINIZ: ", 4*self.score)

    def displayProgress(self):
        totalQuestion =len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print("Quiz bitti!")
        else:
            print(f' {questionNumber}.SORUDASINIZ, TOPLAM {totalQuestion} SORU VAR.'.center(100, "*"))




q1 = Question(" Fatih Sultan Mehmet’in babası kimdir?", ["A) I. Mehmet","B) II.Murat","C) Yıldırım Beyazıt"],"B")
q2 = Question("Hangisi periyodik tabloda bulunan bir element değildir?", ["A) Oksijen","B) Su","C) Azot"],"B")
q3 = Question("Hangisi tarihteki Türk devletlerinden biri değildir?", ["A) Emevi Devleti","B) Hun İmparatorlugu","C) Avar Kaganlığı"],"A" )
q4 = Question(" Galatasaray hangi yıl UEFA kupasını almıştır?", ["A) 2000","B) 2001","C) 2002"],"A")
q5 = Question("Kıbrıs Barış harekatı hangi tarihte gerçekleşmiştir? ", ["A) 1970","B) 1972","C) 1974"],"C")
q6 = Question(" Hangi ülke Asya kıtasındadır? ", ["A) Madagaskar","B) Singapur","C) Peru"],"B")
q7 = Question("Aşağıdaki hangi Anadolu takımı Türkiye Süper Liginde şampiyon olmuştur?", ["A) Bursaspor","B) Kocaelispor","C) Eskişehirspor"],"A")
q8 = Question("Hangisi Kanuni Sultan Süleyman’ın eşidir? ", ["A)Hürrem Sultan","B)Safiye Sultan","C)Kösem Sultan "],"A")
q9 = Question(" Tarihçilerin Kutbu olarak bilinen dünyaca ünlü tarihçimiz kimdir?", ["A) İlber Ortaylı","B) Halil İnalcık ","C) Mehmet Fuat Köprülü"],"C")
q10 = Question("Fransız İhtilali kaç yılında gerçekleşmiştir? ", ["A) 1789-1799","B) 1768-1787","C) 1876-1889 "],"A")
q11= Question("Hangi hayvan memeli değildir? ", ["A) Yarasa","B) Yunus","C) Penguen"],"C")
q12= Question("Hangisi kuvvet birimidir? ", ["A) Joule","B) Newton","C) Pascal"],"B")
q13= Question(" Bir dönem Pelé, Franz Beckenbauer, Carlos Alberto ve Yasin Özdenak ‘ın da oynadığı ABD futbol takımı hangisidir?", ["A) DC United","B) New York Cosmos","C) Los Angeles Galaxy "],"B")
q14= Question("Osmanlı’da Lale devri hangi padişah döneminde yaşamıştır?", ["A) III. Ahmet","B) IV. Murat","C) III.Selim"],"A")
q15= Question("Bir elektrik devresinde direnç hangi harfle gösterilir? ", ["A) D","B) R","C) A"],"B")
q16= Question("Hangisi Kurtuluş Savaşı sırasında gerçekleşmiştir? ", ["A) Kut'ul Amare Zaferi","B) İnönü Zaferi","C) Çanakkale Zaferi "],"B")
q17= Question(" Aşağıdakilerden hangisi Aziz Nesin'in bir eseri değildir?", ["A) Gol Kralı","B) Zübük","C) Yer Demir Gök Bakır "],"C")
q18 = Question("Türk ordusunun ve Türk Kara Kuvvetlerinin kuruluşu hangi yıl kabul edilir?", ["A) M.Ö.209","B) 1071","C) 1919 "],"A")
q19= Question(" İstiklal Marşı hangi yıl yazılmıştır? ", ["A) 1919","B) 1920","C) 1921 "],"C")
q20= Question("Türk Silahlı Kuvvetlerinde hangi rütbe daha yüksektir? ", ["A) Korgeneral","B) Tuğgeneral","C) Tümgrneral"],"A")
questions = [q1, q2, q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20]

quiz = Quiz(questions)
question = quiz.getQuestion()
quiz.loadQuestion()


