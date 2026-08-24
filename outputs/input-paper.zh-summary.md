# Input paper

- Source: https://arxiv.org/abs/2509.04664
- PDF: https://arxiv.org/pdf/2509.04664

## Paragraph Summaries

### Paragraph 1

**中文总结**

大型语言模型在不确定时会猜测，产生可能正确但实际上错误的陈述，这降低了它们的实用性和可信度。这种现象被称为‘幻觉’，主要是由于训练和评估过程倾向于奖励猜测而非承认不确定性。

<details>
<summary>Original paragraph</summary>

Why Language Models Hallucinate
Adam Tauman Kalai∗
OpenAI
Ofir Nachum
OpenAI
Santosh S. Vempala†
Georgia Tech
Edwin Zhang
OpenAI
September 4, 2025
Abstract
Like students facing hard exam questions, large language models sometimes guess when
uncertain, producing plausible yet incorrect statements instead of admitting uncertainty. Such
“hallucinations” persist even in state-of-the-art systems and undermine trust. We argue that
language models hallucinate because the training and evaluation procedures reward guessing over
acknowledging uncertainty, and we analyze the statistical causes of hallucinations in the modern
training pipeline. Hallucinations need not be mysterious—they originate simply as errors in binary
classification. If incorrect statements cannot be distinguished from facts, then hallucinations
in pretrained language models will arise through natural statistical pressures. We then argue
that hallucinations persist due to the way most evaluations are graded—language models are
optimized to be good test-takers, and guessing when uncertain improves test performance. This
“epidemic” of penalizing uncertain responses can only be addressed through a socio-technical
mitigation: modifying the scoring of existing benchmarks that are misaligned but dominate
leaderboards, rather than introducing additional hallucination evaluations. This change may
steer the field toward more trustworthy AI systems. 1 Introduction
Language models are known to produce overconfident, plausible falsehoods, which diminish their
utility and trustworthiness. This error mode is known as “hallucination,” though it differs fundamen-
tally from the human perceptual experience.

</details>

### Paragraph 2

**中文总结**

最新的语言模型仍然存在幻觉问题，即使在请求明确回答时也给出了错误的日期。我们通过计算学习理论来分析这些错误的统计性质。

<details>
<summary>Original paragraph</summary>

Despite significant progress, hallucinations continue to
plague the field, and are still present in the latest models (OpenAI, 2025a). Consider the prompt:
What is Adam Tauman Kalai’s birthday? If you know, just respond with DD-MM. On three separate attempts, a state-of-the-art open-source language model 1 output three incorrect
dates: “03-07”, “15-06”, and “01-01”, even though a response was requested only if known. The
correct date is in Autumn. Table 1 provides an example of more elaborate hallucinations. Hallucinations are an important special case oferrorsproduced by language models, which we
analyze more generally using computational learning theory (e.g., Kearns and Vazirani, 1994). We
consider general sets oferrors E, an arbitrary subset of plausible strings X =E∪V, with the other
plausible stringsV being calledvalid. We then analyze the statistical nature of these errors, and
∗Email:adam@kal.ai
†Supported in part by NSF award CCF-2106444 and a Simons Investigator award. Email:vempala@gatech.edu
1The language model was DeepSeek-V3 (600 B parameters), accessed via the DeepSeek app on 11 May 2025. 1
arXiv:2509.04664v1 [cs.CL] 4 Sep 2025

</details>

### Paragraph 3

**中文总结**

研究指出，语言模型在训练过程中即使使用无错误的数据也会生成错误信息，这被称为幻觉。这种分析适用于广泛的语言模型，并不依赖于特定的预测或Transformer网络特性。

<details>
<summary>Original paragraph</summary>

ChatGPT:
(GPT-4o)
Adam Tauman Kalai’s Ph.D. dissertation (completed in 2002 at CMU) is entitled:
“Boosting, Online Algorithms, and Other Topics in Machine Learning. ”
DeepSeek: “Algebraic Methods in Interactive Machine Learning”. . . at Harvard University in 2005. Llama: “Efficient Algorithms for Learning and Playing Games”. . . in 2007 at MIT. Table 1: Excerpts from responses to “What was the title of Adam Kalai’s dissertation?” from three
popular language models. 3 None generated the correct title or year (Kalai, 2001). apply the results for the type of errors of interest: plausible falsehoods called hallucinations. Our
formalism also includes the notion of apromptto which a language model must respond. The distribution of language is initially learned from a corpus of training examples, which
inevitably contains errors and half-truths. However, we show that even if the training data were
error-free, the objectives optimized during language model training would lead to errors being
generated. With realistic training data containing shades of error, one may expecteven higher
error rates. Thus, our lower bounds on errors apply to more realistic settings, as in traditional
computational learning theory (Kearns and Vazirani, 1994). Our error analysis is general yet has specific implications for hallucination. It applies broadly,
including to reasoning and search-and-retrieval language models, and the analysis does not rely
on properties of next-word prediction or Transformer-based neural networks. It only considers the
two stages of the modern training paradigm: pretraining and post-training, described below.

</details>

### Paragraph 4

**中文总结**

该研究探讨了语言模型的幻觉现象，包括与用户提示矛盾的内在幻觉和与训练数据或现实不符的外在幻觉。研究指出，在预训练过程中，即使使用无误的数据，模型也可能产生错误，这可以通过将其与二元分类问题联系起来进行解释。

<details>
<summary>Original paragraph</summary>

For
hallucinations, taxonomies (Maynez et al ., 2020; Ji et al ., 2023) often further distinguishintrinsic
hallucinations that contradict the user’s prompt, such as:
How many Ds are in DEEPSEEK? If you know, just say the number with no commentary. DeepSeek-V3 returned “2” or “3” in ten independent trials; Meta AI and Claude 3.7 Sonnet 2
performed similarly, including answers as large as “6” and “7” . Our theory also sheds light on
extrinsichallucinations, which contradict the training data or external reality. 1.1 Errors caused by pretraining
During pretraining, abase modellearns the distribution of language in a large text corpus. We show
that, even with error-free training data, the statistical objective minimized during pretraining would
lead to a language model that generates errors. Proving this is nontrivial because some models make
no errors, such as one that always outputs “I don’t know” (IDK) or one that simply memorizes and
reproduces an error-free corpus. Our analysis explains what types of errors should be expected after
pretraining. To do this, we draw a connection to binary classification. Consider questions of the form “Is this
a valid language model output?” Generating valid outputs is in some sense harder than answering
these Yes/No questions, because generation implicitly requires answering “Is this valid” about each
candidate response. Formally, we consider the Is-It-Valid (IIV) binary classification problem which
has a training set consisting of a large number of responses, each labeled either as valid (+) or error
2https://meta.aiandhttps://claude.ai, accessed May 9, 2025. 3The models were freely accessed 2025-05-09 viachatgpt.com, the DeepSeek app (R1, DeepSeek-AI et al., 2025),
andhuggingface.co(Llama-4-Scout-17B-16E-Instruct), respectively.

</details>

### Paragraph 5

**中文总结**

模型没有搜索网络。

<details>
<summary>Original paragraph</summary>

None of the models searched the Web. 2

</details>

### Paragraph 6

**中文总结**

图1展示了Is-It-Valid需要学习识别带有标记±示例的有效生成。语言模型可以被用作IIV分类器，从而建立了生成错误率与IIV误分类率之间的数学关系：生成错误率约等于2倍的IIV误分类率。

<details>
<summary>Original paragraph</summary>

––++++–++++++++++++++––
Valid examples+Greetings.How can I help? There are 2 D’sin LADDER.There is 1 N in PIANO.Mia Holdner’sbirthday is 4/1.I don’t know Zdan’s birthday. Error examples–Greatings.How kaneye help?There are 3 L’sin SPELL.There is 1 G in CAT.Colin Merivale’s birthday is 8/29.Jago Pere’s birthday is 8/21.Birthdays(no pattern)
Counting(poor model)
Spelling(good model)+––
–
–
–
–
+–––
––––
–––––––––
––––––––––––+++++++++++++––––––––––––––+++++++++++––––––
Figure 1: Is-It-Valid requires learning to identify valid generations using labeled ±examples (left). Classifiers (dashed lines) may be accurate on certain concepts like spelling (top) but errors often
arise due to poor models (middle) or arbitrary facts when there is no pattern in the data (bottom). (−), as illustrated in Fig. 1. For this supervised learning problem, both train and test data are
50/50 mixtures of valid examples labeled as + (i.e., the pretraining data since we assume it is valid)
and uniformly random errors from E labeled as−. We then show how any language model can be
used as an IIV classifier. This in turn allows us to establish a mathematical relationship between
generative errors (such as hallucinations) and IIV misclassification rate:
(generative error rate)≳2·(IIV misclassification rate). Language models avoid many types of errors such as spelling mistakes, and not all errors are
hallucinations. The reduction from IIV misclassification to generation illuminates the statistical
nature of generative errors. The analysis shows how pretraining directly contributes to errors. Furthermore, it shows that the samestatistical factorscontributing to errors in binary classification
also cause language model errors.

</details>

### Paragraph 7

**中文总结**

研究显示，分类错误的复杂性包括无模式数据的情况（Domingos, 2012）。我们的分析表明，即使在预训练后，模型仍可能产生自信的幻觉，因为它们倾向于表达确定性而非不确定性。

<details>
<summary>Original paragraph</summary>

Decades of research has shed light on the multifaceted nature
of misclassification errors (Domingos, 2012). Fig. 1 (right) illustrates these factors visually: top,
separable data classified accurately; middle, a poor model of a linear separator for a circular region;
and bottom, no succinct pattern. Section 3.3 analyzes several factors, including the following stylized
setting with epistemic uncertainty, when there is no pattern in the data. This reduction ties together earlier work which covered different types of facts. For example,
Kalai and Vempala (2024) considered a special case of arbitrary facts where there is no learnable
pattern in the data, like the earlier birthday hallucination example. We show how the IIV reduction
covers this case and recovers their bound that the hallucination rate, after pretraining, should be at
least the fraction of training facts that appear once. For instance, if 20% of birthday facts appear
exactly once in the pretraining data, then one expects base models to hallucinate on at least 20% of
birthday facts. In fact, our analysis strengthens their result to include prompts and IDK responses,
both essential components of hallucination. 1.2 Why hallucinations survive post-training
The second stage,post-training, refines the base model, often with a goal of reducing hallucinations. While the analysis of pretraining covered errors more generally, our analysis of post-training focuses
on why overconfident hallucinations are generated rather than omitting information or expressing
uncertainty such as IDK. We offer a socio-technical explanation for the persistence of hallucinations
after post-training and discuss how the field can suppress them. 3

</details>

### Paragraph 8

**中文总结**

人类在不确定时也会猜测或撒谎以获得高分，这与语言模型为了通过二元评分标准而可能产生幻觉类似。现有评估大多惩罚不确定性，导致模型总是处于‘考试模式’。

<details>
<summary>Original paragraph</summary>

As an analogy, consider the following context where humans also occasionally fabricate plausible-
sounding information. When uncertain, students may guess on multiple-choice exams and even
bluff on written exams, submitting plausible answers in which they have little confidence. Language
models are evaluated by similar tests. In both settings, guessing when unsure maximizes the expected
score under a binary 0-1 scheme that awards 1 point for a correct answer and none for blanks or
IDKs. Bluffs are often overconfident and specific, such as “September 30” rather than “Sometime
in autumn” for a question about a date. Many language-model benchmarks mirror standardized
human exams, using binary metrics such as accuracy or pass-rate. Optimizing models for these
benchmarks may therefore foster hallucinations. Humans learn the value of expressing uncertainty
outside of school, in the school of hard knocks. On the other hand, language models are primarily
evaluated using exams that penalize uncertainty. Therefore, they are always in “test-taking” mode. Put simply, most evaluations are not aligned. We are not the first to realize that binary grading does not measure hallucination. However,
prior work on hallucination evaluation has generally sought after the elusive “perfect hallucination
eval. ” In Section 4, we argue that this is insufficient. We observe that existing primary evaluations
overwhelmingly penalize uncertainty, and thus the root problem is theabundance of evaluations
that are not aligned. Suppose Model A is an aligned model that correctly signals uncertainty and
never hallucinates. Let Model B be similar to Model A except that it never indicates uncertainty
and always “guesses” when unsure.

</details>

### Paragraph 9

**中文总结**

模型B在0-1评分基准下将优于A，这导致了对不确定性和弃权的惩罚‘流行病’。研究指出，通过调整评估方法来停止对弃权的惩罚是必要的，并提出了统计上严谨的修改方案以减轻幻觉问题。

<details>
<summary>Original paragraph</summary>

Model B will outperform A under 0-1 scoring, the basis of most
current benchmarks. This creates an “epidemic” of penalizing uncertainty and abstention, which
we argue that a small fraction of hallucination evaluations won’t suffice. The numerous primary
evaluations must be adjusted to stop penalizing abstentions when uncertain. Contributions.We identify the main statistical drivers of hallucinations, from their pretraining
origins to their post-training persistence. A novel connection between supervised and unsupervised
learning demystifies their origin, even when training data contain IDK. The persistence of hallucina-
tions, despite extensive work on the problem, is explained by the recognition that hallucination-like
guessing is rewarded by most primary evaluations. We discuss statistically rigorous modifications to
existing evaluations that pave the way to effective mitigation. 2 Related work
To the best of our knowledge, the reduction from supervised learning (binary classification) to
unsupervised learning (density estimation or self-supervised learning) presented in this work is
novel. The general method of reduction between learning problems, however, is a well-established
technique for demonstrating that one problem is at least as hard as another (see, e.g., Beygelzimer
et al., 2016). A number of surveys and studies have explored the underlying causes of hallucination in
language models. Sun et al . (2025) cite factors such as model overconfidence Yin et al . (2023),
decoding randomness Lee et al . (2022), snowballing effects Zhang et al . (2023), long-tailed training
samples Sun et al . (2023), misleading alignment training Wei et al . (2023), spurious correlations Li
et al. (2022), exposure bias Bengio et al . (2015), the reversal curse Berglund et al .

</details>

### Paragraph 10

**中文总结**

Jeong (2024) 和 Kalai 及 Vempala (2024) 的研究探讨了类似的数据错误来源，这些错误在更广泛的机器学习和统计学领域中也已有长期的研究（Russell 和 Norvig, 2020）。

<details>
<summary>Original paragraph</summary>

(2024), and
context hijacking Jeong (2024). Analogous sources of error have long been studied in broader
machine learning and statistical settings (Russell and Norvig, 2020). The most closely related theoretical work is by Kalai and Vempala (2024), which we show is
4

</details>

### Paragraph 11

**中文总结**

该研究将Good-Turing缺失质量估计与幻觉联系起来，但未涉及不确定性表达、监督学习连接及模型未包含提示。其他研究表明，在保持一致性和生成多样性之间存在权衡，且通过强化学习等技术可以减少幻觉现象。

<details>
<summary>Original paragraph</summary>

a special case of our reduction. They connected the Good-Turing missing mass estimates (Good,
1953) to hallucinations, which inspired Theorem 3. However, that work does not address uncertainty
expressions (e.g., IDK), connections to supervised learning, post-training modifications, and their
model did not include prompts. Hanneke et al . (2018) analyze an interactive learning algorithm
that queries a validity oracle (e.g., a human) to agnostically train a language model that minimizes
hallucinations. Their method is statistically efficient, requiring a reasonable amount of data, but
not computationally efficient. Other recent theoretical studies (Kalavasis et al ., 2025; Kleinberg and
Mullainathan, 2024) formalize an inherent trade-off betweenconsistency(avoiding invalid outputs)
andbreadth(generating diverse, linguistically rich content). These works demonstrate that for broad
classes of languages, any model that generalizes beyond its training data will either hallucinate
invalid outputs or suffer mode collapse, failing to produce the full range of valid responses. Several post-training techniques—such as reinforcement learning from human feedback (RLHF)
(Ouyang et al., 2022), reinforcement learning from AI feedback (RLAIF) (Bai et al., 2022), and direct
preference optimization (DPO) (Rafailov et al ., 2023)—have been shown to reduce hallucinations,
including conspiracy theories and common misconceptions. Gekhman et al . (2024) show that simple
fine-tuning on novel information can initially decrease hallucination rates, only for them to later
increase. Further, it has been demonstrated that both natural language queries and internal model
activations encode predictive signals about factual accuracy and model uncertainty (e.g., Kadavath
et al., 2022).

</details>

### Paragraph 12

**中文总结**

研究指出，通过模型对语义相关查询的一致性检验可以发现或减轻幻觉现象。虽然已有多种方法有效缓解幻觉问题，并且一些基准测试已被引入评估，但关于这些工具的采纳障碍的研究较少。此外，语言模型可以通过更复杂的表达方式来传达不确定性，并且语用学在理解这一点上也变得越来越重要。

<details>
<summary>Original paragraph</summary>

As discussed in our introduction, inconsistencies in a model’s answers to semantically
related queries can also be leveraged to detect or mitigate hallucinations (Manakul et al ., 2023; Xue
et al., 2025; Agrawal et al., 2024). Numerous other methods have proven effective in mitigating hallucinations; see, for example,
the surveys by Ji et al . (2023) and Tian et al . (2024). In terms of evaluation, several comprehensive
benchmarks and leaderboards have recently been introduced (e.g., Bang et al ., 2025; Hong et al .,
2024). However, relatively little work has examined barriers to their adoption. The 2025 AI Index
report (Maslej et al ., 2025), for instance, notes that hallucination benchmarks “have struggled to
gain traction within the AI community. ”
Beyond binary expressions of certainty, more nuanced linguistic constructions have been proposed
to communicate gradations of uncertainty (Mielke et al., 2022; Lin et al., 2022a; Damani et al., 2025). Additionally, the field of pragmatics—which investigates how meaning is shaped by context—has
increasing relevance for understanding and improving how language models convey information (Ma
et al., 2025). 3 Pretraining Errors
Pretraining produces a base language model ˆpthat approximates the distribution text drawn from
its training distribution p. This is the classic “density estimation” problem in unsupervised learning,
where adensityis simply a probability distribution over data. In the case of language models, the
distribution is over text or multimodal inputs if included. The key challenge in proving that base models err is that many language models do not err. The degenerate model which always outputs IDK also avoids errors (assuming IDK is not an error).

</details>

### Paragraph 13

**中文总结**

即使训练数据无误，简单的基模型复述随机训练样本也不会出错，但这些模型在密度估计上失败。最优的基模型匹配训练分布以避免错误，但这并非统计语言模型的基本目标。

<details>
<summary>Original paragraph</summary>

Similarly, assuming error-free training data, the trivial base model which regurgitates text from
a random training example also does not err. However, these two language models fail at density
estimation, the basic goal of statistical language modeling as defined below. Errors are also avoided
by the optimal base model ˆp=p which matches the training distribution, but this model would
5

</details>

### Paragraph 14

**中文总结**

研究表明，即使经过良好训练的基础模型也可能产生某些类型的错误。我们通过计算学习理论的视角分析了这些错误机制，并指出生成有效输出比判断输出有效性更困难。

<details>
<summary>Original paragraph</summary>

require prohibitively large training data. Nonetheless, we show that well-trained base models should
still generate certain types of errors. Our analysis shows that generating valid outputs (i.e., avoiding errors) is harder than classifying
output validity. This reduction enables us to apply the lens of computational learning theory,
where errors are expected and understood, to error mechanisms in generative models. A language
model is initially defined as a probability distribution over text and laterpromptsare incorporated
(Section 3.2); both settings share the same intuition. Examples without prompts include birthday
statements such as those of Fig. 1, while a prompted model might be queried for a specific individual’s
birthday. Not merely autocomplete.Our analysis applies to general density estimation and not only
“next-word predictors” even though many language models are trained usingself-supervised learning
to predict each word based on the previous words. It is tempting to attribute hallucinations to
poorly chosen prefixes (e.g., “Adam Kalai was born on”) for which the language model cannot
provide valid completions. However, from a purely statistical perspective, ignoring computation,
the autocomplete view 4 of language models is no more significant than the fact that any human
speaker produces one word at a time. Our analysis suggests that errors arise from the very fact that
the models are being fit to the underlying language distribution, though the specific architecture
can introduce additional errors. 3.1 The reduction without prompts
Without prompts, a base model ˆpis a probability distribution over a set X . As discussed earlier,
eachexample x∈Xrepresents a “plausible” string, e.g., a document.

</details>

### Paragraph 15

**中文总结**

该研究将实例分为错误样本集E和有效样本集V，定义了基础模型的错误率为err，并引入了IIV二分类问题及其误分类率erriiv。

<details>
<summary>Original paragraph</summary>

5 The examplesX =E∪V
are partitioned into errorsE and valid examplesV, for nonempty disjoint sets E,V . The error rate
of base model ˆpis denoted by,
err := ˆp(E) = Pr
x∼ˆp
[x∈E].(1)
Training data are assumed to come from a noiselesstraining distribution p(X ), i.e., where p(E) = 0. As discussed, with noisy training data and partly correct statements, one may expecteven higher
error ratesthan our lower bounds. We now formalize the IIV binary-classification problem, introduced in the introduction. IIV
is specified by the target function f :X →{−,+}to be learned (membership in V) and the
distributionDover examplesX(a 50/50 mix of samples frompand uniformly random errors):
D(x) :=
{
p(x)/2 ifx∈V,
1/2|E|ifx∈E,andf(x) :=
{
+ ifx∈V,
−ifx∈E. Our analysis lower bounds the error rate err = ˆp(E) in terms of IIV’s aforementionedmisclassifi-
cation rateerr iiv:
erriiv := Pr
x∼D
[
ˆf(x)̸=f(x)
]
,where ˆf(x) :=
{
+ if ˆp(x)>1/|E|,
−if ˆp(x)≤1/|E|. (2)
4Mathematically, any distribution p induces a distribution of completions p(wiwi+1 . . .|w1w2 . . . wi−1 ) for every
prefix of wordsw 1 . . . wi−1 in its support. 5We assume thatXis finite for simplicity. See Section 5 for further discussion of errors and plausibility. 6

</details>

### Paragraph 16

**中文总结**

该基础模型通过阈值化概率作为IIV分类器使用。对于任何训练分布和基础模型，误差下界公式表明所有基础模型都会在未学习的IIV事实（如生日）上出错，这些事实的误差率较大且δ和|V|/|E|较小。

<details>
<summary>Original paragraph</summary>

The base model is thus used as an IIV classifier, in our reduction, by thresholding the base model’s
probability at a certain threshold 1/|E|. Note that such probabilities ˆp(x) can generally be efficiently
computed for base models (though efficient computation is not necessary for the lower-bounds to be
meaningful). Corollary 1.For any training distributionpsuch thatp(V) = 1and any base modelˆp,
err≥2·erriiv−|V|
|E|−δ,
forerr,err iiv from Eqs.(1)and(2), andδ:=|ˆp(A)−p(A)|forA:={x∈X |ˆp(x)>1/|E|}. Since this relationship holds foranybase model ˆp, it immediately implies that all base models
will err on inherently unlearnable IIV facts (such as the birthdays absent from the training data)
where erriiv is necessarily large, and where δand|V|/|E|are small (e.g., for each person there are
364 times more incorrect birthday claims in E than correct ones in V, plus IDK). The corollary
above follows immediately as a special case of Theorem 1 which covers the more general case with
prompts. Theorem 2 later uses this general result to provide lower-bounds for an intuitive special
case. Theorems 3 and 4 address small |E|, e.g.,|E|= 1 for True/False questions. The constant 2 in
the above bound is relatively tight: for large |E|and small δ, erriiv could be near 1/2 for unlearnable
concepts while err≤1. Corollary 1 also implies that erriiv ≲1/2. Hallucination errors.To apply the error analysis to hallucinations, one may consider E to be
the set of plausible generations containing (one or more) plausible falsehoods. Note that a common
alternate definition of hallucinations is asgenerations that are not grounded in the training data(or
prompt).

</details>

### Paragraph 17

**中文总结**

该研究指出，由于假设训练数据有效，生成的事实错误无法基于事实正确的训练数据。通过比较实际样本和合成生成的样本来估算δ值，可以验证模型的校准情况。

<details>
<summary>Original paragraph</summary>

Fortunately, the lower-bound above also applies to this notion because we have assumed
only valid training data, i.e., a generated factual error cannot be grounded in factually correct
training data. Calibration.We now argue why |δ|is a measure of (mis)calibration that is small after pretraining. Note thatwithout any knowledge of the language, one can achieve δ= 0 by simply taking the
uniform distribution ˆp(x) = 1/|X|, and thus δ= 0 does not require p = ˆp. An auditor can trivially
estimate δby comparing the fractions of responses satisfying ˆp(x)> 1/|E|versus ˆp(ˆx)> 1/|E|using
sets of training samples x∼pand synthetic generations ˆx∼ˆp. Inspired by Dawid (1982), one may
think of an analogy to a weather forecaster predicting the probability of rain each day. A minimal
calibration requirement would be whether their average prediction matched the average fraction
of rain. One could also require these two to match on days when the forecast was > tfor some
thresholdt∈[0, 1]. Dawid (1982) introduced the more stringent requirement that forevery t∈[0, 1],
among days on which the prediction istit rains about atfraction of the time. Here is a particularly simple justification for why δis typically small for the standard pretraining
cross-entropy objective,
L(ˆp) =Ex∼p[−log ˆp(x)].(3)
Consider rescaling the probabilities of the positively-labeled examples by a factor s > 0 and
normalizing:
ˆps(x) :∝
{
s·ˆp(x) if ˆp(x)>1/|E|,
ˆp(x) if ˆp(x)≤1/|E|. 7

</details>

### Paragraph 18

**中文总结**

图2展示了强化学习前后的GPT-4概率直方图，预训练模型表现良好校准。研究指出，对于足够强大的语言模型而言，在标准交叉熵目标下，局部优化会导致较大的误差δ，这表明校准和错误是自然结果。实验结果显示，基础模型通常较为校准，而经过强化学习的模型则可能偏离交叉熵目标。

<details>
<summary>Original paragraph</summary>

Figure 2: GPT-4 calibration histograms before (left) and after (right) reinforcement learning
(OpenAI, 2023a, Figure 8, reprinted with permission). These plots are for multiple-choice queries
where the plausible responses are simply A, B, C, or D. The pretrained model is well calibrated. Then, a simple calculation shows that δis the magnitude of the derivative of the loss with respect
to the scaling factors, evaluated ats= 1:
δ=
⏐⏐⏐⏐
d
dsL(ˆps)
⏐⏐⏐
s=1
⏐⏐⏐⏐. If δ̸= 0, then rescaling by some s̸= 1 would reduce the loss, so the loss is not at a local minimum. For any class of language models powerful enough to approximate such simple rescaling, local
optimization should yield small δ. Note that δ, being defined at a single threshold t = 1/|E|is
weaker than notions such as Expected Calibration Error (ECE) which integrate over thresholdst. Hallucinations are inevitableonly for base models.Many have argued that hallucinations
are inevitable (Jones, 2025; Leffer, 2024; Xu et al ., 2024). However, a non-hallucinating model
could be easily created, using a question-answer database and a calculator, which answers a fixed
set of questions such as “What is the chemical symbol for gold?” and well-formed mathematical
calculations such as “3 + 8”, and otherwise outputs IDK. Moreover, the error lower-bound of
Corollary 1 implies that language models which do not err must not be calibrated, i.e., δmust be
large. As our derivations show, calibration—and, hence, errors—is a natural consequence of the
standard cross-entropy objective. Indeed, empirical studies (Fig. 2) show thatbase modelsare often
found to be calibrated, in contrast to post-trained models which may deviate from cross-entropy in
favor of reinforcement learning.

</details>

### Paragraph 19

**中文总结**

我们扩展了第3.1节的设置，包括来自分布µ的提示c∈C。每个示例x现在由一个提示c和一个可能的回答r组成。这相当于当µ将概率分配为1/8的情况。

<details>
<summary>Original paragraph</summary>

3.2 The reduction with prompts
Henceforth, we generalize the setting of Section 3.1 to include prompts (contexts) c∈Cdrawn
from aprompt distribution µ. Each example x = (c,r ) now consists of a prompt c and plausible
response r. The analysis above corresponds to the special case in which µassigns probability 1
8

</details>

### Paragraph 20

**中文总结**

对于给定的提示c，定义Vc为有效响应集，Ec为错误响应集。训练分布和基础模型被视为条件响应分布p(r|c)和ˆp(r|c)，并通过联合分布p(c,r)和ˆp(c,r)扩展。尽管假设训练数据包含来自相同提示分布的模型对话是不现实的，但当此假设失效时，可能会出现更高的错误率。

<details>
<summary>Original paragraph</summary>

to the empty prompt. For a given prompt c∈C, letVc :={r|(c,r )∈V}be the valid responses
andEc :={r|(c,r )∈E}be the erroneous responses. The training distribution and base model
are now conditional response distributions p(r|c),ˆp(r|c). For notational convenience, we extend
these to joint distributions on X byp(c,r ) :=µ(c)p(r|c) and ˆp(c,r ) :=µ(c)ˆp(r|c), so that still
err := ˆp(E) =∑
(c,r)∈Eµ(c)ˆp(r|c) andp(E) = 0. Training distribution examples therefore correspond to valid “dialogues,” as in the case of
distillation (Chiang et al ., 2023; Anand et al ., 2023). Although assuming that the training data
contain model dialogues drawn from the same prompt distribution is unrealistic, even higher error
rates may be expected when the assumption fails. The IIV problem with prompts has the same
target functionf(x) := + iffx∈V, but the generalized distribution D selects, with equal probability
either x∼por x = (c,r ) for c∼µand uniformly random r∈Ec. Finally, the classifier ˆf(c,r ) is
now + iff ˆp(r|c)>1/minc|Ec|. Corollary 1 is thus clearly a special case of,
Theorem 1.For any training distributionpsuch thatp(V) = 1and any base modelˆp,
err≥2·erriiv−maxc|Vc|
minc|Ec|−δ,
whereδ:=|ˆp(A)−p(A)|forA:={(c,r)∈X |ˆp(r|c)>1/minc|Ec|}. Generalizing the rescaling ˆps(r|c) (normalizing per prompt, still with single parameter s) again
justifies a smallδ=
⏐⏐ d
dsL(ˆps)|s=1
⏐⏐, now forL(ˆp) := ∑
(c,r)∈X−µ(c) log ˆp(r|c). 3.3 Error factors for base models
Decades of research have elucidated the statistical factors contributing to misclassifications (errors
in binary classification).

</details>

### Paragraph 21

**中文总结**

我们可以通过先前的理解来列举幻觉和其他生成错误的原因，包括统计复杂性、模型不足以及GIGO等因素。例如，在随机任意事实的情况下，当没有简洁的模式可以解释目标函数时，训练数据中可能缺乏必要的知识。

<details>
<summary>Original paragraph</summary>

We can leverage this prior understanding to enumerate factors behind
hallucinations and other generative errors, including: statistical complexity, as in birthdays (Sec-
tion 3.3.1);poor models, as in letter counting (Section 3.3.2); and additional factors like GIGO, as
in conspiracy theories (Section 3.4). 3.3.1 Arbitrary-fact hallucinations
When there is no succinct pattern that explains the target function, there is epistemic uncertainty
meaning that necessary knowledge is absent from the training data. The Vapnik-Chervonenkis
dimension (Vapnik and Chervonenkis, 1971) VC(F) characterizes the worst-case number of examples
needed to learn a family F of functions f :X →{−,+}, with high probability. Families with
high VC(F) dimension may require prohibitively many samples to learn. We consider a natural
special case of high VC dimension: random arbitrary facts. In particular, this section considers
valid responses (other than IDK) which are random and independent across prompts. Definition 1(Arbitrary Facts).The following are fixed: an arbitrary prompt distribution µ(c), an
IDKresponse and, for each promptc: a response setR c and a probability of answeringαc∈[0,1]. Independently for each c, a single correct answer ac∈Rc is chosen uniformly at random. Finally,
p(ac|c) =αc andp(IDK|c) = 1−αc for eachc∈C. ThusEc =R c\{ac}andVc ={ac,IDK}. It is assumed that there is a single way to write any given fact, which can be done as in the lead
birthday example where the format was specified. However, we again note that one may expecteven
9

</details>

### Paragraph 22

**中文总结**

该研究基于单例率定义了hallucinations的下限，通过训练数据中仅出现一次的提示比例来估算模型生成未见过事实的概率。对于任意事实模型，任何算法在给定N个训练样本后输出估计值ˆp，其误差概率大于99%时满足特定公式。存在一个高效算法可输出校准的ˆp，同样以高概率满足另一个误差界限。

<details>
<summary>Original paragraph</summary>

more hallucinationswith multiple ways to state each fact. In the case of fixed-format birthdays,
|Ec|= 364 and notable people whose birthdays are discussed often would have high µ(c). Notable
birthdays like Einstein’s appear multiple times, whereas others may only occur once, e.g., in an
obituary. Large language models seldom err on frequently referenced facts, e.g., Einstein’s birthday
or dissertation title. Our lower-bound for hallucinations is based on the fraction of prompts appearing just once in
the training data, ignoring IDKs. Definition 2(Singleton rate).A prompt c∈Cis asingletonif it appears exactly once in the N
training data
⟨
(c(i),r (i))
⟩N
i=1 without abstention, i.e., |{i:c(i) =c∧r(i)̸= IDK}|= 1. Let S⊆C
denote the set of singletons and
sr =|S|
N
denote the fraction of training singletons. The singleton rate builds on Alan Turing’s elegant “missing-mass” estimator (Good, 1953), which
gauges how much probability is still assigned to outcomes that have not yet appeared in a sample
from a distribution. Concretely, Turing’s estimate of the unseen-event probability is the fraction of
samples appearing exactly once. Intuitively, singletons act as a proxy for how many more novel
outcomes you might encounter in further sampling, so their empirical share becomes the estimate
for the entire “missing” portion of the distribution. We now state our bounds for Arbitrary Facts. Theorem 2(Arbitrary Facts).In the Arbitrary Facts model, any algorithm which takes N training
samples and outputs ˆpsatisfies, with probability≥99%over ⃗ a=⟨ac⟩c∈Cand the N training examples:
err≥sr−2
minc|Ec|−35 + 6 lnN√
N
−δ. Moreover, there is an efficient algorithm outputting calibrated ˆp(δ= 0) that with probability ≥99%,
err≤sr− sr
maxc|Ec|+ 1+ 13√
N
.

</details>

### Paragraph 23

**中文总结**

早期版本的论文中缺少了提示和弃权的相关定理证明(Kalai和Vempala，2024)，后续研究(Miao和Kearns，2025)则进行了幻觉、单例率和校准的实证研究。

<details>
<summary>Original paragraph</summary>

An earlier version of this paper presented a related theorem that omitted prompts and abstentions
(Kalai and Vempala, 2024). The proof is in Section B. Follow-up work by Miao and Kearns (2025)
provides an empirical study of hallucinations, singleton rate, and calibration. 3.3.2 Poor models
Misclassifications can also arise when the underlying model is poor because: (a) the model family
cannot represent the concept well, such as linear separators approximating circular regions, or (b)
the model family is sufficiently expressive but the model itself is not a good fit. Agnostic Learning
(Kearns et al., 1994) addresses (a) by defining the minimal error rate of any classifier in a given
familyGof classifiersg:X→{−,+}:
opt(G) := min
g∈G
Pr
x∼D
[g(x)̸=f(x)]∈[0,1]. 10

</details>

### Paragraph 24

**中文总结**

如果opt(G)较大，则G中的任何分类器都将有较高的误分类率。对于每个上下文只有一个正确响应的标准多项选择题，定理3表明即使在C=2的选择中也能达到误差边界。以三元语言模型为例，证明了其生成错误率至少为1/2。

<details>
<summary>Original paragraph</summary>

If opt(G) is large, then any classifier in G will have high misclassification rate. In our case, given
a language model ˆpθparameterized by θ∈Θ, consider the family of thresholded-language-model
classifiers:
G:=
{
gθ,t
⏐⏐ θ∈Θ,t∈[0,1]
}
,whereg θ,t(c,r) :=
{
+ if ˆp θ(r|c)>t,
−if ˆpθ(r|c)≤t. It follows immediately from Theorem 1 that
err≥2·opt(G)−maxc|Vc|
minc|Ec|−δ. When exactly one correct response exists per context (i.e., standard multiple choice, without IDK),
the calibration term can be removed and bounds can be achieved even forC= 2 choices. Theorem 3(Pure multiple-choice).Suppose |Vc|= 1for all c∈Cand let C = minc|Ec|+ 1be the
number of choices. Then,
err≥2
(
1−1
C
)
·opt(G)
To illustrate, consider the classic trigram language model where each word was predicted based
only on the prior two words, i.e., a context window of just two words. Trigram models were
dominant in the 1980s and 1990s. Trigram models, however, regularly output ungrammatical
sentences. Consider the following prompts and responses:
c1 = She lost it and was completely out of... c 2 = He lost it and was completely out of... r1 = her mind.r 2 = his mind. Here,V c1 :=E c2 :={r1}andVc2 :=E c1 :={r2}. Corollary 2.Let µbe uniform over{c1,c 2}. Then any trigram model must have a generation error
rate of at least 1/2. This follows from Theorem 3 because C = 2 and opt(G) = 1/2 for trigram models. The proofs
of Theorem 3 and Corollary 2 are in Section C. Although n-gram models can capture longer-range
dependencies for largern, data requirements scale exponentially inn. We now revisit the letter-counting example from the introduction.

</details>

### Paragraph 25

**中文总结**

研究显示，DeepSeek-R1模型在计算字母数量上表现更好，表明它更适合此类任务。现代语言模型通常以词元而非单个字符来表示提示，这提出了一个表示上的挑战。

<details>
<summary>Original paragraph</summary>

To see that this is a poor
model issue, note that the DeepSeek-R1 reasoning model reliably counts letters, e.g., producing a
377-chain-of-thought that includes:
Let me spell it out: D-E-E-P-S-E-E-K. First letter: D — that’s one D. Second letter: E — not D. Third letter: E — not D. . . So, the number of Ds is 1. Assuming similar training data, this suggests that R1 is a better model for the task than the DeepSeek-
V3 model. One representational challenge that reasoning overcomes is that modern language models
represent prompts bytokens, e.g., D/EEP/SEE/K, rather than individual characters (DeepSeek-AI
et al., 2025). 11

</details>

### Paragraph 26

**中文总结**

错误可能是由多种因素共同导致的，包括计算难度、分布偏移以及GIGO效应。AI系统在解决计算难题时可能会出错；数据分布差异可能导致模型对未见过的问题给出错误答案；训练数据中的错误也可能被语言模型复制。

<details>
<summary>Original paragraph</summary>

3.4 Additional factors
Errors may occur due to a combination of multiple factors, including the ones discussed above and
several others. Here, we highlight a few. • Computational Hardness. No algorithm run on a classical computer, even an AI with
superhuman capabilities, can violate the laws of computational complexity theory. Indeed,
AI systems have been found to err on computationally hard problems (Xu et al ., 2024). Observation 2 of Section D illustrates how Theorem 1 applies to intractable queries of the
form“What is the decryption ofc?”and IDK is a valid answer. • Distribution shift. A well-known challenge in binary classification is that training and test
data distributions often diverge (Qui˜ nonero-Candela et al., 2009; Moreno-Torres et al ., 2012). Analogously, errors in language models often stem from out-of-distribution (OOD) prompts
that differ substantially from the training distribution. A question such as, “What’s heavier, a
pound of feathers or a pound of lead?” may be unlikely in the training data and may induce
erroneous answers in certain models. Similarly, distribution shift could be a factor in the
letter-counting example above, though the fact that reasoning models correctly count letters
suggests that the poor models may be a greater factor. • GIGO: Garbage in, Garbage out. Large training corpora often contain numerous factual
errors, which may be replicated by base models. The statistical similarity of GIGO for both
classification and pretraining is self evident, and hence we do not provide a formal treatment. However, it is important to recognize GIGO among statistical factors, as language models
have been shown to replicate errors from training data (Lin et al ., 2022b; Levy et al ., 2021;
Alber et al., 2025).

</details>

### Paragraph 27

**中文总结**

GIGO还自然地过渡到后训练主题，这可以减少某些错误，如常见的误解和阴谋论。尽管后训练应使模型从类似于自动完成的模型转变为不输出自信的谬误（除非适当），但现有基准测试和排行榜实际上可能加剧幻觉问题，因此需要改变评估标准并获得广泛认可。

<details>
<summary>Original paragraph</summary>

GIGO also offers a natural segue to the topic of post-training, which decreases certain GIGO
errors, such as common misconceptions and conspiracy theories (Ouyang et al ., 2022; OpenAI,
2023a; Costello et al ., 2024). The next section explains why some hallucinations persist—and may
even be exacerbated—by current post-training pipelines. 4 Post-training and hallucination
Post-training should shift the model from one which is trained like an autocomplete model to one
which does not output confident falsehoods (except when appropriate, e.g., when asked to produce
fiction). However, we claim that further reduction of hallucinations is an uphill battle, since existing
benchmarks and leaderboards reinforce certain types of hallucination. We therefore discuss how
to stop this reinforcement. This is a socio-technical problem in the sense that, not only do the
existing evaluations need to be modified, but these changes need to be adopted in the influential
leaderboards. 4.1 How evaluations reinforce hallucination
Binary evaluations of language models impose a false right-wrong dichotomy, award no credit
to answers that express uncertainty, omit dubious details, or request clarification. Such metrics,
including accuracy and pass rate, remain the field’s prevailing norm, as argued below. Under binary
12

</details>

### Paragraph 28

**中文总结**

在给定问题时，最优策略不是选择弃权。现有评估可能需要调整，因为大多数流行的评估都采用二元评分方式，这可能导致诚实地报告信心和不确定性时出现幻觉。

<details>
<summary>Original paragraph</summary>

grading, abstaining is strictly sub-optimal. IDK-type responses are maximally penalized while an
overconfident “best guess” is optimal. The motivation combines two desirable factors: (a) the rate
of accuracy among what is output by the language model, and (b) how comprehensive responses
are. However, weighing (a) more than (b) is important for reducing hallucinations. Formally, for any given question in the form of a prompt c, denote the set of plausible responses
(valid or error) byRc :={r|(c,r )∈X}. Further, suppose there is a set of plausible abstention
responsesAc⊂Rc (e.g., IDK). Agrader gc :Rc→Ris said to bebinaryif {gc(r)|r∈Rc}={0, 1}
and gc(r) = 0 for all r∈Ac. Aproblemis defined by ( c,Rc,Ac,gc) where the test-taker knows
c,Rc,Ac. We assume that the test-taker knows that the rubric is binary but is not told the correct
answers, where gc(r) = 1. The test-taker’s beliefs about the correct answer can be viewed as a
posterior distribution ρc over binary gc’s. For any such beliefs, the optimal response is not to
abstain. Observation 1.Let c be a prompt. For any distribution ρc over binary graders, the optimal
response(s) are not abstentions, i.e.,
Ac∩arg max
r∈Rc
Egc∼ρc
[gc(r)] =∅. Although the proof is trivial (see Section E), Observation 1 suggests thatexisting evaluations
may need to be modified. Table 2 summarizes the short meta-evaluation analysis in Section F,
finding that the vast majority of popular evaluations have binary grading. Therefore, additional
hallucination evaluations may not suffice when the primary evaluations penalize honestly reporting
confidence and uncertainty.

</details>

### Paragraph 29

**中文总结**

该研究指出，即使理想的心理评估和训练方法能够产生诚实的不确定性报告，但如果大多数现有评估的表现不佳，则这些优势可能仍会被掩盖。为此，建议明确在评估说明中设定置信度目标，并在提示中注明，以鼓励参与者仅在确信时作答。

<details>
<summary>Original paragraph</summary>

This does not diminish existing work on hallucination evaluations but
rather points out that even the ideal hallucination evaluation and ideal post-training methodology,
yielding honest reports of uncertainty, may still be drowned out because of inferior performance on
the vast majority of the existing evaluations. 4.2 Explicit confidence targets
Human tests are similarly mostly binary, and it has been recognized that they also reward overcon-
fident bluffing. Of course, exams are only a small component of human learning, e.g., fabricating
birthdays will quickly result in embarrassment. Nonetheless, some standardized national exams
operate or have operated using penalties for incorrect answers (or equivalently partial credit for
abstaining), including Indian JEE, NEET, and GATE exams; AMC tests from the Mathematical
Association of America; and US standardized SAT, AP, and GRE tests in earlier years. Importantly,
the grading system is clearly stated in the instructions, and test takers are often aware of the
confidence threshold beyond which it makes sense to make their best guess. Similarly, we propose evaluations explicitly stateconfidence targetsin their instructions, within
the prompt (or system message). For example, one could append a statement like the following to
each question:
Answer only if you are >t confident, since mistakes are penalized t/(1−t) points, while
correct answers receive 1 point, and an answer of “I don’t know” receives 0 points. There are several natural values of t including t = 0.5 (penalty 1), t = 0.75 (penalty 2), and t = 0.9
(penalty 9). A threshold of t = 0 corresponds to binary grading and could be described by, e.g.,
“Make your best guess even if you are unsure, as if you were taking an exam. ” A simple calculation
13

</details>

### Paragraph 30

**中文总结**

该研究分析了多种评估基准，其中大多数不给予错误推测任何分数，并且也不为不确定的回答提供信用。只有少数基准如IFEval和Omni-MATH允许部分得分或根据置信度给出不确定回答一定的分数。

<details>
<summary>Original paragraph</summary>

Table 2: Summary of evaluation benchmarks analyzed in this work and their treatment of
abstentions. “Binary grading” indicates that the primary metric is a strict correct/incorrect
accuracy; “IDK credit” denotes whether abstentions can earn any credit. Benchmark Scoring method Binary grading IDK credit
GPQA Multiple-choice accuracy Yes None
MMLU-Pro Multiple-choice accuracy Yes None
IFEval Programmatic instruction verification Yes a None
Omni-MATH Equivalence grading ∗ Yes None
WildBench LM-graded rubric ∗ No Partial b
BBH Multiple-choice / exact-match Yes None
MATH (L5 split) Equivalence grading ∗ Yes None
MuSR Multiple-choice accuracy Yes None
SWE-bench Patch passes unit tests Yes None
HLE Multiple-choice / equivalence grading ∗ Yes None
∗ Grading is performed using language models, hence incorrectbluffsmay occasionally be scored as correct. a IFEval aggregates several binary rubric sub-scores into a composite score. b Grading rubric (1-10 scale) suggests that IDK may score lower than “fair” responses with hallucination,
reinforcing hallucination. shows that the expected score of offering an answer beats IDK (score 0) iff its confidence (i.e.,
probability of being correct) is>t. Such penalties have been well-studied within hallucination research (Ji et al ., 2023). However,
we suggest two subtle variations which have statistical ramifications. First, we propose making
the confidence threshold explicit in the instructions, whereas the prior work has largely omitted
mentioning the confidence targets or penalties in the instructions. (A notable exception is the work
of Wu et al .

</details>

### Paragraph 31

**中文总结**

该研究建议明确指定置信度阈值，以支持客观评分，并提出将置信度目标纳入现有主流评估中，如SWE-bench，这可以减少对适当表达不确定性的惩罚。

<details>
<summary>Original paragraph</summary>

(2025) who introduce “risk-informing” prompts with explicit penalties.) The ideal
penalty might reflect likely real-world harms, but that is impractical as it is specific to the problem,
the target application, and the user group. Without transparent specification within the instructions,
it would be difficult to achieve consensus among language-model creators on the correct thresholds. Similarly, students might bicker that grading is unfair given instructions that there is an unspecified
penalty for errors. Instead, specifying confidence thresholds explicitly in each problem’s instructions
supports objective grading even if the specific thresholds chosen are somewhat arbitrary or even
random. A single model may be best across all thresholds, if the threshold is explicit. However, if
the threshold is not stated, then there is an inherent tradeoff, and no single model will be best in
general (other than one that is always correct). Second, we suggest incorporating confidence targets into existing mainstream evaluations, such
as the popular SWE-bench (Jimenez et al ., 2024) which involves binary grading of software patches,
while the majority of prior work has introduced implicit error penalties in bespoke hallucination
evaluations. Merely adding evaluations with implicit error penalties faces the aforementioned
accuracy-error tradeoff. On the other hand, incorporating confidence targets into the established
evaluations, already in use, reduces the penalty for appropriate expressions of uncertainty. It may
thus amplify the effectiveness of hallucination-specific evaluations. With explicit confidence targets, there is one behavior which is simultaneously optimal for all
targets—outputting IDK among examples where its correctness probability is greater than the
14

</details>

### Paragraph 32

**中文总结**

行为校准是指模型必须给出至少具有t信心的最有用的回答，而不是输出概率置信度。虽然现有模型可能并未表现出行为校准，但它可以作为客观评估的一种方法。

<details>
<summary>Original paragraph</summary>

target. Let us refer to this asbehavioral calibration–rather than requiring the model to output a
probabilistic confidence (Lin et al ., 2022a), it must formulate the most useful response in which
it is at least t confident. Behavioral calibration can be audited by comparing accuracy and error
rates across thresholds, and circumvents the problem that there may be exponentially many ways to
phrase correct responses (Farquhar et al., 2024). Existing models may or may not exhibit behavioral
calibration, but it may prove useful as an objective evaluation. 5 Discussion and limitations
It is difficult for the field to agree upon how to define, evaluate and reduce hallucinations due to
their multifaceted nature. A statistical framework must prioritize certain aspects and omit others,
for simplicity. Several notes are in order about the extent and limitations of the framework used
herein. Plausibility and nonsense.A hallucination is a plausible falsehood, and by considering only
plausible stringsX , our analysis ignores the possibility of generating nonsensical strings (which
state-of-the-art language models rarely generate). However, the statement and proof of Theorem 1
hold with the modified definitions of nonsensical examples N with partition X =N∪E∪V,
err := ˆp(N∪E),D(N) = 0, and the assumption thatp(V) = 1. Open-ended generations.For simplicity, the examples presented in this paper are oriented
towards a single factual question. However, hallucinations often arise for open-ended prompts,
such as “Write a biography about. . . . ” This can be fit into our framework by defining a response
containing one or more falsehoods to be an error. However, in such a case it would be natural to
consider degrees of hallucination depending on how many errors there are.

</details>

### Paragraph 33

**中文总结**

研究表明，搜索或RAG增强的语言模型可以减少幻觉现象，但这一方法并非万能。某些错误无法仅通过提示和响应来判断，且现有框架未能区分不同级别的不确定性。

<details>
<summary>Original paragraph</summary>

Search (and reasoning) are not panaceas.A number of studies have shown how language
models augmented with search or Retrieval-Augmented Generation (RAG) reduce hallucinations
(Lewis et al., 2020; Shuster et al ., 2021; Nakano et al ., 2021; Zhang and Zhang, 2025). However,
Observation 1 holds for arbitrary language models, including those with RAG. In particular, the
binary grading system itself still rewards guessing whenever search fails to yield a confident answer. Moreover, search may not help with miscalculations such as in the letter-counting example, or other
intrinsic hallucinations. Latent context.Some errors cannot be judged by the prompt and response alone. For example,
suppose a user asks a question about phones and the language model provides a response about
cellphones, but the question was intended to be about land lines. Such ambiguities do not fit our
error definition which does not depend on context external to the prompt and response. It would be
interesting to extend the model to allow for “hidden context” that are not part of the prompt given
to the language model, but which could be used for judging errors, relating toaleatoric uncertainty. A false trichotomy.Our formalism does not distinguish between errors of different magnitudes or
degrees of uncertainty. Clearly, the correct/incorrect/IDK categories are also incomplete. Although
the statistical ideal might be to score each evaluation just as we would like to score the language model
in the downstream application, explicit confidence targets offer a practical, objective modification
to mainstream evaluations, and a false trichotomy may at least offer an IDK option unlike a false
dichotomy. 15

</details>

### Paragraph 34

**中文总结**

这篇论文探讨了现代语言模型幻觉的统计因素，从预训练中的生成错误到后训练中幻觉的持续存在。通过调整主流评估标准，可以鼓励更准确地表达不确定性，从而减少幻觉现象，并为具有更丰富语用能力的语言模型的研究铺平道路。

<details>
<summary>Original paragraph</summary>

Beyond IDK.There are numerous ways to signal uncertainty, such as hedging, omitting details,
and asking questions. Ultimately language models may adhere to confidence notions such as
linguistic calibration (Mielke et al ., 2022; Damani et al ., 2025). However, the pragmatic phenomena
of language (Austin, 1962; Grice, 1975) are nuanced. For example, while there are instances where
it may be useful for language models to explicitly state probabilistic confidence estimates (Lin et al .,
2022a), this can also lead to unnatural utterances, such as, “I’m 1/365 certain that Kalai’s birthday
is March 7th. ” The present paper focuses on the statistical factors regarding the top-level decision
of what is said. 6 Conclusions
This paper demystifies hallucinations in modern language models, from their origin during pretraining
to their persistence through post-training. In pretraining, we show that generative errors parallel
misclassifications in supervised learning, which are not mysterious, and naturally arise due to the
minimization of cross-entropy loss. Many language model shortcomings can be captured by a single evaluation. For example, overuse
of the opener “Certainly” can be addressed by a single“Certainly” eval(Amodei and Fridman,
2024) because starting responses with “Certainly” does not significantly impact other evaluations. In contrast, we argue that the majority of mainstream evaluations reward hallucinatory behavior. Simple modifications of mainstream evaluations can realign incentives, rewarding appropriate
expressions of uncertainty rather than penalizing them. This can remove barriers to the suppression
of hallucinations, and open the door to future work on nuanced language models, e.g., with richer
pragmatic competence (Ma et al., 2025).

</details>

### Paragraph 35

**中文总结**

感谢Alex Beutel等多位同事提供的有益讨论。

<details>
<summary>Original paragraph</summary>

Acknowledgments.We would like to thank Alex Beutel, Tom Cunningham, Yann Dubois,
Parikshit Gopalan, Johannes Heidecke, Zoe Hitzig, Saachi Jain, Manas Joglekar, Sanjay Kairam,
Ehud Kalai, Amin Karbasi, Alan Luo, Anay Mehrotra, Eric Mitchell, Cameron Raymond, David G. Robinson, Mandip Shah, Joshua Vendrow, Grigoris Velegkas, Rose Wang, Zhigang Wang, Jason
Wolfe, and Jason Wei for helpful discussions.

</details>
