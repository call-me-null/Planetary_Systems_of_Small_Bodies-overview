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
  Small Bodies in Solar System
</div>

<div class="cover-line"></div>

<div class="cover-subtitle">
  
</div>

---
layout: default
class: bg-white text-black
---

## Small Bodies

<div class="grid grid-cols-10 gap-8 items-start">

  <div class="col-span-3">

<p class="mb-4">
小天体とは，惑星と自然衛星を除いたすべての自然天体である．
</p>

<ul>
  <li>彗星</li>
  <li>小惑星</li>
  <li>太陽系外縁天体（カイパーベルト帯天体，ケンタウルス天体など）</li>
  <li>隕石</li>
  <li>塵</li>
  <li>準惑星</li>
  <li>トロヤ群</li>
  <li>...</li>
</ul>

  </div>

  <div class="col-span-7 flex justify-center">
    <img src="/solar system.png" class="w-full max-w-xl rounded-lg" />
  </div>

</div>

---

## Solar System

<div class="w-full h-[calc(100%-3rem)] flex justify-center items-center">
  <img src="/PIA17046_-_Voyager_1_Goes_Interstellar.jpg" class="max-w-full max-h-full object-cover" />
</div>

---

<h1 class="mt-0 mb-1">小惑星帯，カイパーベルト，オールト雲の位置</h1>

<div class="w-full h-[calc(100%-8rem)] flex justify-center items-center">
  <img src="/Small_objects_in_the_Solar_System.jpg" class="scale-114 object-contain" />
</div>

**カイパーベルト**：海王星軌道（30.2AU）外側，小天体が密集するドーナツ状の領域

**オールト雲**：太陽系外部球殻状と考えられている天体群である．

---

<div class="float-right ml-6 mb-4 mr-0 w-80 translate-y-4">
  <img src="/Lagrange_very_massive.png" class="w-full rounded-lg" />
  <p class="text-xs text-center mt-1 text-gray-600">
    Figure: Trojans near the Lagrange points $L_4$ and $L_5$
  </p>
</div>

### Centarus ケンタウルス天体

木星と海王星の間に存在する天体

<div class="grid grid-cols-2 gap-6">

<div>

$$
\text{木星} < 
\begin{matrix}
\text{近点距離} \\
\\
\text{軌道長半径}
\end{matrix}
< \text{海王星}
$$

</div>

<div>

- 不安定な軌道
- 海王星以遠に起源

</div>

</div>

カイパーベルト起源し，巨大惑星に引かれて太陽系の「内側」に入る天体である．中間的なグループで，$10^8 \sim 10^9$年経って結局は木星族彗星（JFCs）・太陽系から脱出

### Trojans トロヤ群

- 惑星の前後$60^\circ$付近（ラグランジュ点$L_4, L_5$の近く）に安定に存在する小天体群

<div class="clear-both"></div>


---


# Why Do We Study Small Bodies?

小天体は太陽系の初期の情報を保存している重要な存在

- 物質的：海王星以遠の小天体の成分は，太陽系が形成する時期の外縁部の情報を反映している．
> The composition of the solid bodies beyond Neptune's orbit reflects the early enviroment in the edge of the proto-solar disk.

- 力学的：成分だけでなく，小天体の軌道構成は昔の情報を反映する．
> the orbital evolution of the objects reflects the formation history of the plantary system.

- 太陽系とそれ以外の宇宙環境との相互作用

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

### The Three-body Problem

3つの天体が互いに重力で影響し合う運動

### 円制限三体問題
- 質量の大きい2つの天体
- 3つ目の天体は質量が非常に小さく，無視する

### Tisserand parameter
制限三体問題において保存量
$$
T_J = \frac{a_J}{a} + 2\sqrt{ \left( (1 - e^2)\frac{a}{a_J} \right)} \cos i
$$
ここで，$a, e, i$ はそれぞれ彗星軌道の半長軸、離心率、軌道傾斜角；$a_J = 5.2 \,\mathrm{AU}$は木星軌道の長半径である．LPCsは $T_J \leq 2$，SPCsは $2 < T_J \leq 3$ を満たす．

---

### Kuiper Belt

カイパーベルトの範囲は，海王星軌道（約30 $AU$）付近の内縁を持ち，観測でよくわかってないが数千$AU$まで広がっている．特に散乱円盤成分は短周期彗星，とくに木星族彗星の主な供給源と考えられている．カイパーベルト天体は太陽系形成時の力学進化の情報を保持しているため，その軌道分布は太陽系初期史を調べる手がかりになる．
$f \propto r_H^{-4}$
散乱光で観測される天体のフラックス密度は，太陽からの距離4乗に反比例するため，
$$
f \propto r_H^{-4}
$$
大きさが$~100km$程度の天体が$10^{5}$個，$1km$以上の天体が$10^{10}$個と推測される．

### Oort Cloud

オールト雲は長周期彗星の起源であり，$~10^{12}$個の彗星が含まれると思われている．球状(spherical swarm)の天体の集まりで，直径が$~10^5 AU$．オールト雲についてはよく知られていなく，太陽系内側に入る彗星の軌道から推測されている．



---

### 銀河潮汐による摂動時間スケール

通過する天体の質量が$M_*$，相対速度$V_*$，最近接距離$d$をして，彗星のと通過天体の距離の関数が
$$
R = \sqrt{d^2 + V_* t}
$$
となり，最近接距離方向上の加速度
$$
a = \frac{GM_*}{R^2} \cdot \frac{d}{R}
$$
速度の変化（スカラー）$\Delta V$は
$$
\begin{aligned}
\Delta V
&= \int \frac{G M_*}{R^2} \cdot \frac{d}{R}\, dt \\
&= \int \frac{G M_* d}{(d^2 + V_* t)^{3/2}}\, dt 
\end{aligned}
$$
変数変換
$$
u = \frac{V_*t}{d}
$$

---

$$
\begin{aligned}
\Delta V = \frac{GM_*}{dV_*} \int^{+\infty}_{-\infty} \frac{du}{(1+u^2)^{3/2}}
\end{aligned}
$$
置換積分
$$
u = \tan{\theta} \\
du = \frac{1}{\cos^2{\theta}}d\theta = \sec^2{\theta}d\theta
$$
を使って，積分部分は
$$
\begin{aligned}
\begin{aligned}
\int_{-\infty}^{+\infty} \frac{du}{(1+u^2)^{3/2}}
&= \int_{-\pi/2}^{+\pi/2}
\frac{\sec^2\theta}{\sec^3\theta}\,d\theta 
= \int_{-\pi/2}^{+\pi/2} \cos\theta\,d\theta 
= \left. \sin\theta \right|_{-\pi/2}^{+\pi/2}
= 2 .
\end{aligned}
\end{aligned}
$$
$$
\Delta V = \frac{2GM_*}{dV_*} 
$$
となる．
$G = 6.6 \times 10^{-11} \,\mathrm{N\,kg^{-2}\,m^2}$，
$M_* = 2\times10^{30} \,\mathrm{kg}$，
$V_* = 20 \,\mathrm{km\,s^{-1}}$，
$d = 1\,\mathrm{pc} = 3\times10^{16}\,\mathrm{m}$を代入すると
$$
\Delta V \sim 1 \,\mathrm{m\,s^{-1}}
$$

---

$10^5AU$におけるケプラー速度は$V_K \sim 93.8 m/s$.

銀河潮汐による摂動時間スケール$N \sim (\frac{V_K}{\Delta V})^2　 = 10^4 yr$ となる． 


---

<div class="grid grid-cols-10 gap-8 items-start mt-6">

<div class="col-span-4">

最近第三の彗星供給源が小惑星帯に発見した．ここに氷を含む小惑星が予想外に生き残っている．「メインベルト彗星(main-belt comets)」と呼ぶ．


</div>

<div class="col-span-6 flex justify-center">
  <img src="/fig1.jpeg" class="w-full max-w-md rounded-lg" />
</div>

</div>

彗星の運命は小惑星と似てて，太陽また惑星と衝突；太陽から脱出する；自我崩壊することである．

歴史的理由から，水星は多くのグループに分類される．名称はそれぞれ性質を表さない．
Damocloids（ダモクレス族）は消滅した長周期彗星である．ケンタウルス天体はカイパーベルトから脱出し，太陽系の惑星領域（特に巨大惑星の領域）に入った天体である．木星起動を超えたケンタウルス天体は木星族彗星と呼ぶ．非活動的木星族彗星はdJFCs（また彗星軌道上小惑星，ACOs）と呼ぶ．

彗星に重要なのは，力学的と化学的性質である．



---

## 彗星の破壊

前に紹介したように，彗星の破壊過程（メカニズム）が3つある．簡単に，衝突・脱出・崩壊である．

木星族彗星を例として，力学的半減期$\tau_d \sim 0.4 \,\mathrm{Myr}$と考えられている．しかし，この長く存在すると，彗星の軌道傾斜角は現在より広く分布する．

実際の半減期は$\tau \sim 12{,}000$である．なぜ$\tau \ll \tau_d$かを調べる必要となる．

### 昇華
輻射輸送から調べる．彗星の輻射平衡方程式は
$$
\frac{F_\odot}{r_H^2} = \chi \sigma T^4 +\chi f_s(T)H(T)
$$
である．ここで，$F_\odot = \int F_{\nu} d\nu$太陽の全周波数のエネルギーを表す．
右辺の第一項で，$\chi$は形状修正係数，彗星の形状に依存する．$\varepsilon\sigma T^4$は彗星を黒体とみなし，放射するエネルギーである．

右辺第二項は，熱に関するもので，$f_s(T)$が二相平衡状態についての関数である．$H(T)$は潜熱．

---

$$
f_s =\frac{F_\odot-\chi \sigma T^4 r_H^2}{\chi H(T) r_H^2}
$$
$r_H \to 0$を取ると
$$
f_s \sim \frac{F_\odot(1-A)}{\chi H(T) r_H^2}
$$
となる．すなわち$f_s \propto r_H^{-2}$である．

この時，彗星の直径を$r_n$として，$f_A$が昇華する面積と表面積との比例で，彗星の消えるまでの時間は
$$
\tau_{\text{sub}} \sim \frac{\rho_n r_n}{3 f_s f_A}
$$
>$\tau_{\text{sub}}$導出不能

水氷の場合，$r_H = 3$AUにおいて，$f_s \sim 3 \times 10^{-5}$\,kg\,m$^{-2}$\,s$^{-1}$となり，$\rho_n = 500$\,kg\,m$^{-3}$半径1kmの核は$\tau_{\text{sub}} \sim 10^{12} \sim 10^5$yearsである．



--- 


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