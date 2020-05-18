from tag_skill.services.text_preprocess_extractor import text_preprocesing_emsi, text_preprocesing_summerizer
from tag_skill.services.emsi_skill_extractor import extract_skills
from tag_skill.services.text_summerizer import summerize, pos_tagger
from tag_skill.services.TextRank import TextRank4Keyword
from tag_skill import config_file
import json
from skill_tagging.settings import BASE_DIR
import os

loacalskill_filepath = BASE_DIR + '/tag_skill/resources/'


class handlerClass():
    def __init__(self):
        self.final_list = list()

    def processHandler(self, input_data):

        if os.path.exists(loacalskill_filepath + 'local_skills.txt'):
            if os.stat(loacalskill_filepath + 'local_skills.txt').st_size != 0:
                with open(loacalskill_filepath + 'local_skills.txt') as f:
                    local_skills = [line.rstrip() for line in f]
            else:
                print('File is Empty')
                local_skills = list()
        else:
            open(loacalskill_filepath + 'local_skills.txt', 'a').close()
            local_skills = list()

        if config_file.emsi_skill_extrcator == 'enabled':
            clean_data1 = text_preprocesing_emsi(input_data)
            returned_skills = extract_skills(clean_data1)
            returned_skills = json.loads(returned_skills)
            for value in returned_skills['skills']:
                if value['skill']['type'] == 'Hard Skill':
                    skill_dict = {'tag': value['skill']['name'], 'type': 'require_skill', 'source': 'external_EMSI'}
                    self.final_list.append(skill_dict)
                if value['skill']['name'] not in local_skills:
                    local_skills.append(value['skill']['name'])
            with open(loacalskill_filepath + 'local_skills.txt', 'w') as filehandle:
                filehandle.writelines("%s\n" % place for place in local_skills)

        if config_file.problem_domain_extractor == 'enabled':
            clean_text2 = text_preprocesing_summerizer(input_data)
            print()
            summerized_text = summerize(clean_text2)
            print(summerized_text)

            print(len(summerized_text))  ## 700
            tr4w = TextRank4Keyword()
            tr4w.analyze(summerized_text.lower(), candidate_pos=['NOUN'], window_size=6, lower=False)
            word_list = tr4w.get_keywords(10)
            print(word_list)
            if len(word_list) < 3:
                idx = len(word_list)
            else:
                idx = 4
            for i in range(idx):
                domain_dict = {'tag': word_list[i], 'type': 'problem_domain', 'source': 'custom'}
                self.final_list.append(domain_dict)

        if config_file.summary_phrase == 'enabled':
            summary_phrase = pos_tagger(summerized_text.lower())
            summary_dict = {'tag': summary_phrase, 'type': 'summary_phrase', 'source': 'custom'}
            self.final_list.append(summary_dict)
        return self.final_list
