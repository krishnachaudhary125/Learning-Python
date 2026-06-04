def analyze_text(text):
	# Analyze a given text string and return statistics.
	clean = text.lower().strip()
	words = clean.split()
	chars = [c for c in clean if c.isalpha()]
	vowels = [c for c in chars if c in "aeiou"]
	sentences = text.split(".")

	# Word frequency
	freq = {w: words.count(w) for w in set(words)}
	top3 = sorted(freq, key = lambda w: freq[w], reverse = True)[:3]

	return{
		"total_chars" : len(text),
		"total_words" : len(words),
		"unique_words" : len(set(words)),
		"total_sentences" : len([s for s in sentences if s.strip()]),
		"vowels" : len(vowels),
		"top_3_words" : top3,
		"is_all_lower" : text == text.lower()
	}

sample = "Mero Kitta is a digital platform developed to provide online land and property-related services in Nepal. It helps citizens access maps, land records, and official documents without visiting offices physically. The main objective is to digitize land management services and make them faster, transparent, and user-friendly. It also reduces paperwork, corruption, and long waiting times in government offices. Users can view land maps, request field book prints, plot registers, and track application status online. The system connects survey offices digitally for easier access to land information. Many users face issues like server downtime, slow performance, and limited digital literacy. Internet dependency and technical errors can also affect service accessibility in rural areas."
result = analyze_text(sample)
for k, v in result.items():
	print(f"{k:20}: {v}")