import re


def get_slot(sentence):
    slot_pat = re.compile(r'/(.+?);(.+?)/') # slot 부분만 추출 정규 표현식
    slot_sentence = slot_pat.findall(sentence)

    return slot_sentence

def pre_sentence(sentence):
    space_pat = re.compile(r'/') # 두 개의 slot이 붙어있는 경우를 위한 정규 표현식 (ex. /DEP;서울//ARR;부산/ -> /DEP;서울/ /ARR;부산/)
    del_pat = re.compile(r'[A-Z]+|/|;|_') # slot 중 태그 부분만 추출 정규 표현식

    sentence = space_pat.sub('/ ', sentence) # 붙어있는 슬롯 띄어쓰기
    sentence = del_pat.sub('', sentence)  # 온전한 문장만 생성
    
    return sentence

def get_seq_in(sentence, tokenizer):
    tokens = tokenizer.tokenize(sentence)

    return tokens

def get_seq_out(tokens, slot_sentence, tokenizer):
    seq_out = [] # seq_out 담을 리스트
    seq_out_index = 0 # seq_out에 담기 위한 인덱스
    token_idx = 0 # 전체 문장 토큰 인덱스
    slot_idx = 0 # 전체 문장 중 슬롯의 개수 인덱스
    slot_tokens_idx = 0 # 슬롯 단어의 토큰 인덱스
    tokens_len = len(tokens) # 전체 토큰 개수
    slot_len = len(slot_sentence) # 전체 슬롯 개수

    for token_idx in range(tokens_len):
        # 전체 슬롯 개수보다 슬롯 개수 인덱스 작을 때만 토크나이즈
        if slot_idx < slot_len:
            slot_tokens = tokenizer.tokenize(slot_sentence[slot_idx][1]) #['_회', '진']
            slot_tokens_len = len(slot_tokens) # 하나의 슬롯의 토큰 개수
        # 실제 토큰과 슬롯 토큰이 일치할때만 seq_out에 tag 저장
            if tokens[token_idx] ==  slot_tokens[slot_tokens_idx]: 
                seq_out.append(slot_sentence[slot_idx][0])
                slot_tokens_idx += 1

                # 현재 슬롯 토큰을 다 탐색하면 다음 슬롯 탐색
                if slot_tokens_idx == slot_tokens_len:
                    slot_idx += 1
                    slot_tokens_idx = 0 
                    
                    continue
            else:
                seq_out.append('0')

        # 슬롯에 없는 토큰은 0으로 저장
        else:
            seq_out.append('0')

    # 만약 seq_out과 전체 토큰의 개수가 맞지 않는다면 return 'error'
    if len(seq_out) != tokens_len:
        return 'error'
    else:
        return seq_out



