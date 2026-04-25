---
theme: default
colorSchema: light
background: white
class: bg-white text-black
drawings:
  persist: false
transition: slide-left
comark: true
---

<style>
.slidev-layout {
  background: white !important;
  color: black !important;
}

/* academic cover style */
.cover-title {
  font-family: "Times New Roman", Georgia, serif;
  font-size: 2.6rem;
  font-weight: 600;
  text-align: center;
  letter-spacing: 0.01em;
  line-height: 1.2;
  margin-top: 4rem;
  margin-bottom: 1rem;
  color: #111;
  white-space: nowrap;
}

.cover-subtitle {
  font-family: Arial, Helvetica, sans-serif;
  font-size: 1.2rem;
  font-weight: 400;
  text-align: center;
  letter-spacing: 0.08em;
  color: #444;
  margin-bottom: 2.5rem;
}

.cover-line {
  width: 180px;
  height: 1px;
  background: #888;
  margin: 0 auto 2rem auto;
}
</style>

<div class="cover-title">
  Planetary Systems of Small Bodies
</div>

<div class="cover-line"></div>

<div class="cover-subtitle">
  Overview
</div>

---
layout: default
class: bg-white text-black
---

# Introduction

<div class="grid grid-cols-2 gap-6 items-center">

<div>

小天体は太陽系の初期の情報を保存している重要な存在

- 研究対象：太陽系内の小天体　~100AU

<!--
1. Introduction

The small bodies of the Solar System are carriers of information from the earliest epochs and,
therefore, objects of great scientific interest.

> small bodies とはなんですか？定義は？ $\rightarrow$ 小天体は太陽系の初期の情報を保存している重要な存在
> earliest epochsとは具体的にはいつのことですか？
> なぜ、small bodies 以外は information from the earliest epochs を持っていないのですか？

-->

- 目的・意味：原始的な天体が多く，太陽系初期の情報が得られる
- 特徴：反射率が小さく観測しにくい

<!--
Observationally, the small body populations tend to be difficult to study, both because small means “faint”,
and because many of the bodies of greatest interest (the Kuiper belt objects, the Centaurs, the Trojans)
are far-away residents of the middle and outer Solar System, rendering them fainter still.

> ”faint” とはどういう意味ですか？ ほのかな，かすかな；観測しにくいことを表す
> far-away とはどれくらいの距離のことを言っていますか？
　 - Kuiper Belt: beyond the orbit of Neptune(over 30.2AU)
   -  the Centaurs: q_J < q < q_N; a_J < a < a_N
> the Kuiper belt objects, the Centaurs, the Trojans とはなんですか？定義は？
> middle and outer Solar Systemとはどの領域ですか？
> そもそも、太陽系にはどのような天体がどこまで広がっていますか？
 - 彗星
 - 小惑星・小惑星帯
 - ケンタウルス天体
 - カイパーベルト
 - オールト雲
 - 木星トロヤ


This is why we can study self-luminous objects at the edge of the universe,
but we can barely glimpse what’s in the Kuiper belt only 100 AU away.
It’s also why the study of the small body populations is very fresh and new.

> self-luminous objects とはなんですか？


> 100AU とはどこですか？Kuiper belt以外の太陽系の天体はどれくらいの距離にありますか？


-->

NASA JPLより小天体とは，惑星と自然衛星を除いたすべての自然天体である．

</div>

<div>

<img src="/solar_system.jpg" class="w-full rounded-lg" />

</div>

</div>

---
transition: slide-up
level: 2
---

# The Comets 彗星

<p style="color: black !important; opacity: 1 !important;">
  太陽系外縁から供給される小天体．起源は3つカイパーベルト，オールトの雲，小惑星帯
</p>

<table style="margin: 0 auto; width: 70%; border-collapse: collapse;">
  <tbody>
    <tr>
      <th style="border: 1px solid #999; padding: 8px; text-align: center; font-weight: 700; vertical-align: middle;">
        短周期彗星 SPCs
      </th>
      <th style="border: 1px solid #999; padding: 8px; text-align: center; font-weight: 700; vertical-align: middle;">
        長周期彗星 LPCs
      </th>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        P &lt; 200
      </td>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        P &gt; 200
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        小さい軌道傾斜角と離心率
      </td>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        等方的分布，最大e=1
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        順行
      </td>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        順行・逆行
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        カイパーベルト（KB）
      </td>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        オールト雲(OC)
      </td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        軌道が「水平」
      </td>
      <td style="border: 1px solid #999; padding: 8px; text-align: center; vertical-align: middle;">
        軌道が「傾いている」
      </td>
    </tr>
  </tbody>
</table>

彗星は多くのグループに分類される．例えば，ダモクレス族，木星族，ケンタウルス天体など

ハレー型彗星（HTCs）：3つ目のグループ．力学的な性質が中間的，例えば，P1/ハレー彗星，$P=76$年，$i$がSPCsように$162^\circ$

---

### 2体問題

|  P1の運動方程式   |   P2の運動方程式    |
| --- | --- |
|  $m_1 \frac{d^2}{dt^2} = -Gm_1 m_2 \frac{\mathbf{r}_2-\mathbf{r}_1}{r^3}$  |   $m_2 \frac{d^2}{dt^2} = Gm_1 m_2 \frac{\mathbf{r}_2-\mathbf{r}_1}{r^3}$|

$\mathbf{r}_C = \mathbf{r}_2- \mathbf{r}_1$ を代入して
$$
\mathbf{r}_1 = \mathbf{r}_C - \frac{m_2}{m_1+m_2} \mathbf{r} \\[0.6em]
\mathbf{r}_2 = \mathbf{r}_C + \frac{m_2}{m_1+m_2} \mathbf{r}
$$
すなわち
$$
\frac{d^2r}{dt^2} = - \mu \frac{\mathbf{r}}{r^3}\\[0.6em]
\mu = G(m_1+m_2)
$$

---

### 三体問題
3つの天体が互いに重力で影響し合う運動
### 円制限三体問題
- 質量の大きい2つの天体
- 3つ目の天体は質量が非常に小さく，無視する

### Tisserand parameter
制限三体問題において保存量
$$
T_J = \frac{a_J}{a} + 2 \left( (1 - e^2)\frac{a}{a_J} \right)^{1/2} \cos i
$$
ここで，$a, e, i$ はそれぞれ彗星軌道の半長軸、離心率、軌道傾斜角；$a_J = 5.2 \,\mathrm{AU}$は木星軌道の長半径である．LPCsは $T_J \leq 2$，SPCsは $2 < T_J \leq 3$ を満たす．

---

## 軌道の散乱

オールト雲はLPCsの供給源である．オールト雲には次のことが明確
- $10^{12}$個の彗星
- $10^5 AU$の半径スケール
- もともと円盤であった．10億年わたって球状に

現在，オールト雲の半径，構造，カイパーベルトとの境界に詳しくない

質量 $M_*$、相対速度 $V_*$、最近接距離 $d$ をもつ通過恒星は、OC内を公転する彗星の速度に
$$
\Delta V \sim \left( \frac{2GM_*}{V_* d} \right)^{1/2}
$$
程度の摂動を与える．$G = 6.6 \times 10^{-11} \,\mathrm{N\,kg^{-2}\,m^2}$, $M_* = 2\times10^{30} \,\mathrm{kg}$, $V_* = 20 \,\mathrm{km\,s^{-1}}$, $d = 1\,\mathrm{pc} = 3\times10^{16}\,\mathrm{m}$を代入
$$
\Delta V \sim 1 \,\mathrm{m\,s^{-1}}
$$

---

$10^5 AU$における公転速度は$V_K \sim 100 \,\mathrm{m\,s^{-1}}$である．$V_K$にたつまで$N \sim \left( \frac{V_K}{\Delta V} \right)^2$回の接近が必要であり，$N \sim 10^4$．
実際は銀河潮汐により，10億年を要する．この時間スケールにおいて，惑星軌道面と同じ平面にあった円盤のOCは，等方的な球状分布となった．

<div class="grid grid-cols-10 gap-8 items-start mt-6">

<div class="col-span-4">

最近第三の彗星供給源が小惑星帯に発見した．ここに氷を含む小惑星が予想外に生き残っている．「メインベルト彗星(main-belt comets)」と呼ぶ．

彗星（小天体）の「生まれる」から「死ぬ」まで，様々なグループに分類される．

</div>

<div class="col-span-6 flex justify-center">
  <img src="/fig1.jpeg" class="w-full max-w-md rounded-lg" />
</div>

</div>

彗星集団の関係を示す模式図である．右の時間スケールは，寿命を表す．

---

## 彗星の破壊
彗星の起源を進んでいるが，破壊過程は十分分かっていない．主要なメカニズムは
- 惑星と衝突
- 星間空間へ放出
- 自我崩壊

木星族彗星の力学的半減期$\tau_d$は$\sim 0.4 \,\mathrm{Myr}$程度．しかし観測により，実際12,000 years．この大違いの理由は「エネルギー」
太陽からのエネルギーの使い道は3つ
- 反射
- 熱放射
- 氷の昇華

--- 

## エネルギーバランスの式

$$
\frac{F_\odot}{r_H^2}(1 - A) = \chi \left[ \varepsilon \sigma T^4 + f_s(T) H(T) \right]
$$
左辺$F_\odot = 1360 \,\mathrm{W\,m^{-2}}$は太陽定数，$r_H$は単位AUで表す太陽からの距離，$A$は反射率．輸入したエネルギー<br>
右辺の
- $\varepsilon \sigma T^4$を熱放射，赤外線として逃げるエネルギー
- $f_s(T) H(T)$昇華速度と潜熱
- $1 \le \chi \le 4$，吸収されたエネルギーが表面にどのように分布する無次元量

## 球状天体臨界回転周期

$P_c = \left( \frac{3\pi}{G\rho_n} \right)^{1/2}$

$\rho_n = 500 \,\mathrm{kg\,m^{-3}}$の場合，$P_c \sim 4.7 \,\mathrm{hours}$となる．これより速く回転すると，重力では遠心力に耐えられず崩壊する．

---

# 小惑星

## スペクトルと組成の勾配

小惑星帯に小惑星の組成は太陽からの距離によって異なる．
- 内側(~2AU)：S型(stony)，岩石組成・光学的に赤く（高温）・明るい（反射率0.15）
- 外側(3AU付近)：C型(carbonaceous)，炭素組成・スペクトルはより中性的・暗い（反射率0.05）
このことは距離によって太陽放射の温度の低下だけで説明できない．${}^{26}\mathrm{Al}$（半減期0.7 Myr）の崩壊で加熱されることが広く受け入れられる．${}^{26}\mathrm{Al}$は初期太陽系の熱源となる．
- 内側：早く形成$\rightarrow$加熱効果が強い，水がない
- 外側：遅く形成$\rightarrow$形成時${}^{26}\mathrm{Al}$少ない$\rightarrow$加熱効果が弱い，含水鉱物・氷が残っている

$\Rightarrow$$\Rightarrow$<strong>原始惑星盤の密度が半径増加と共に密度低く</strong>

同位体測定によって，小惑星の組成は連続的に変わることではなく，2つのグループに分かれる理由は小惑星が異なる場所に形成された可能性が高い．

仮説：木星が境界線．内側S型，外側C型．

---

<div class="col-span-6 flex justify-center">
  <img src="/fig6.jpeg" class="w-full max-w-md rounded-lg" />
</div>

彗星（青い点）と小惑星（黄色い点）の分布．赤い丸は活動的小惑星を示す．小惑星の軌道を持ちながら，質量放出のために見た目が彗星に似ている天体である．

縦の破線は火星と木星の軌道長半径である．曲線は遠日点が木星・火星近日点に等しい点の軌跡である．この曲線上の天体は火星・木星の軌道を横切るため，短寿命である．

---

## 活動的小惑星

Active asteroidsとは，彗星のように塵や尾が見える小惑星である．形成は衝撃・ガス放出・昇華・温度変化．


### 衝撃

小惑星帯に衝撃が起こる速度差は$\Delta V \sim 5 \,\mathrm{km\,s^{-1}}$，しかしこの場所の公転速度は$V_K \sim 20 \,\mathrm{km\,s^{-1}}$である．かなりはやい速度．小惑星の軌道は軌道傾斜角と離心率が異なるため，交差した軌道の間に高速衝撃が起こる．

### 回転の不安定性

温度上昇による放出したガスが小惑星の回転を加速する．この加速が遅い．

### 熱崩壊Thermal destruction
岩石は温度変化による膨張・収縮が繰り返し，崩壊する．

---

### 昇華

軌道形状問わず，小惑星は太陽に近づくと（近日点付近）活動再開する（ガス噴出）．代表例である133P/Elst-Pizarroは表面近くに埋もれた氷の昇華によって活動していると考えられ，メインベルト彗星（MBCs）と呼ばれる．しかしこの証拠は間接的である．噴出したガスが現在の分光観測で検出できないため証拠が間接的である．

<strong>彗星と活動的小惑星の区別は，後者は3 AUのほぼ円軌道を持ち，表面温度が氷の長期的に残せる．</strong>

---

# カイパーベルト

<p style="color: black !important; opacity: 1 !important;">
  カイパーベルト天体(KBOs)は太陽系外縁天体の集まりではなく，力学的にいくつかのグループに分類される．
</p>

<div class="col-span-6 flex justify-center">
  <img src="/fig8.jpeg" class="w-full max-w-md rounded-lg" />
</div>

---

<div class="grid grid-cols-2 gap-6 items-center">

  <div class="flex justify-center">
    <img src="/fig8.jpeg" class="w-full max-w-md rounded-lg" />
  </div>

  <div>
    <ul>
      <li>Cは古典的KBO(classical KBOs)：これは、発見前に想像されていた「外側の降着円盤」に最も近い軌道を持つ集団．離心率$e$，傾斜角$i$が比較的に小さい</li>
      <li>Sは散乱天体：近日点が$30 \sim 40\,\mathrm{AU}$，海王星の摂動を強く受ける．離心率up, 内側に入る</li>
      <li>Cenはケンタウルス天体：木星軌道と交わる．一部は彗星になる．</li>
      <li>Dは分離天体 detached objects：近日点が海王星より遠く，起源は謎</li>
    </ul>
  </div>

</div>

グラフに縦方向に積み重なるように分布する天体は，共鳴天体である．例えば，Plutinosは 39 AU における 3:2 で海王星と共鳴運動している．海王星が2週する間にPlutinosが3週公転する．
共鳴KBOの数が多いことは，海王星の外向き移動に伴う共鳴掃引（resonance sweeping）が起こったことを示唆している．

---

## 未発見の惑星

軌道長半径が大きいKBOはランダムではないように見えるため，太陽系外側に未発見の惑星が存在する可能性がある．

## 巨大惑星トロヤ群

トロヤ群とは，惑星とほぼ同じ公転軌道を周りながら，惑星の前後$60^\circ$付近（ラグランジュ点$L_4, L_5$の近く）に安定に存在する小天体群である．

トロヤ群の起源は2つの仮説がある．
- 巨大惑星は近くで形成された微惑星を捕獲した説
- 太陽系外縁起源し，捕獲された説

現時点ではどちらか決定的な証拠がない．