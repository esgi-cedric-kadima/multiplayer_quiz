import html


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.current_question = None
        self.players = []

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        answers = self.current_question.wrong_answers
        answers.append(self.current_question.answer)
        answers.sort()
        answers_text = [html.unescape(answer) for answer in answers]
        return f"Q.{self.question_number}: {q_text}", answers_text

    def check_answer(self, player_name, user_answer):
        player = next((p for p in self.players if p.name == player_name), None)
        if player is None:
            player = Player(player_name)
            self.players.append(player)

        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            player.score += 1
            return True
        else:
            return False

    def get_leaderboard(self):
        self.players.sort(key=lambda x: x.score, reverse=True)
        return [(p.name, p.score) for p in self.players]
