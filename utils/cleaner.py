import re
import math

def cleaning(text):
    if isinstance(text, str): 
        text = text.lower()
        text = re.sub(r'[^ ,.?!a-z0-9àáảãạăắằẳẵặâấầẩẫậèéẻẽẹêếềểễệđìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ]', '', text)
        text = re.sub(r'[.!?]+', '.', text)
        text = re.sub(r'([,.!?])\1+', r'\1', text)
        text = re.sub(r'[,]+', ' , ', text)
        text = re.sub(r'[.]+', ' . ', text)
        text = re.sub(r'([ ])\1+', r'\1', text)
        return text
    return text

