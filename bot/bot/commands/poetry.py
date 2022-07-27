# import torch
# from transformers import AutoTokenizer, AutoModelForCausalLM
#
# tokenizer = AutoTokenizer.from_pretrained('/home/anton/telegram_bot/models/tokenizer_tg/')
# model = AutoModelForCausalLM.from_pretrained("/home/anton/telegram_bot/models/model_for_tg")
#
# prefix = "однажды в студеную зимнюю пору"
#
# tokens = tokenizer(prefix, return_tensors='pt')
#
# size = tokens['input_ids'].shape[1]
# output = model.generate(
#     **tokens,
#     #end_token=end_token_id,
#     do_sample=False,
#
#     max_length=size+500,
#     repetition_penalty=5.,
#     temperature=0.8,
#     num_beams=10,
# )
#
# decoded = tokenizer.decode(output[0])
# result = decoded[len(prefix):]
# print(prefix + result)
