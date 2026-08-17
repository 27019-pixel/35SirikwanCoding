<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MoneyPlan - จัดสรรเงินรายเดือน</title>

  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: "Segoe UI", Tahoma, sans-serif;
    }

    body {
      background: #f5f7fb;
      color: #1e293b;
    }

    .app {
      display: flex;
      min-height: 100vh;
    }

    /* SIDEBAR */
    .sidebar {
      width: 250px;
      background: #111827;
      color: white;
      padding: 25px 18px;
      position: fixed;
      height: 100vh;
      left: 0;
      top: 0;
    }

    .logo {
      font-size: 24px;
      font-weight: 800;
      margin-bottom: 45px;
      padding-left: 12px;
    }

    .logo span {
      color: #22c55e;
    }

    .menu {
      list-style: none;
    }

    .menu li {
      margin-bottom: 10px;
    }

    .menu a {
      color: #9ca3af;
      text-decoration: none;
      display: flex;
      gap: 13px;
      padding: 13px 14px;
      border-radius: 10px;
      transition: .2s;
    }

    .menu a:hover,
    .menu a.active {
      background: #1f2937;
      color: white;
    }

    /* MAIN */
    .main {
      margin-left: 250px;
      width: calc(100% - 250px);
      padding: 30px 40px;
    }

    .topbar {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 30px;
    }

    .topbar h1 {
      font-size: 28px;
    }

    .month {
      background: white;
      border: 1px solid #e5e7eb;
      padding: 10px 15px;
      border-radius: 10px;
    }

    /* SUMMARY */
    .cards {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 18px;
      margin-bottom: 25px;
    }

    .card {
      background: white;
      padding: 22px;
      border-radius: 16px;
      box-shadow: 0 3px 15px rgba(0,0,0,.04);
    }

    .card .label {
      color: #64748b;
      font-size: 14px;
      margin-bottom: 10px;
    }

    .card .value {
      font-size: 26px;
      font-weight: 800;
    }

    .green {
      color: #16a34a;
    }

    .red {
      color: #dc2626;
    }

    .blue {
      color: #2563eb;
    }

    .purple {
      color: #7c3aed;
    }

    /* GRID */
    .grid {
      display: grid;
      grid-template-columns: 1.5fr 1fr;
      gap: 20px;
    }

    .panel {
      background: white;
      padding: 25px;
      border-radius: 16px;
      box-shadow: 0 3px 15px rgba(0,0,0,.04);
      margin-bottom: 20px;
    }

    .panel-header {
      display: flex;
      justify-content: space-between;
      margin-bottom: 25px;
      align-items: center;
    }

    .panel-header h2 {
      font-size: 18px;
    }

    .btn {
      background: #16a34a;
      color: white;
      border: none;
      padding: 10px 15px;
      border-radius: 9px;
      cursor: pointer;
      font-weight: 600;
    }

    .btn:hover {
      background: #15803d;
    }

    /* BUDGET */
    .budget-item {
      margin-bottom: 20px;
    }

    .budget-top {
      display: flex;
      justify-content: space-between;
      margin-bottom: 8px;
    }

    .budget-name {
      font-weight: 600;
    }

    .budget-money {
      color: #64748b;
      font-size: 14px;
    }

    .progress {
      height: 9px;
      background: #e5e7eb;
      border-radius: 20px;
      overflow: hidden;
    }

    .progress-bar {
      height: 100%;
      border-radius: 20px;
    }

    .food {
      width: 72%;
      background: #f97316;
    }

    .home {
      width: 45%;
      background: #3b82f6;
    }

    .travel {
      width: 30%;
      background: #8b5cf6;
    }

    .shopping {
      width: 60%;
      background: #ec4899;
    }

    /* EXPENSE */
    .expense {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 13px 0;
      border-bottom: 1px solid #f1f5f9;
    }

    .expense-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .icon {
      width: 42px;
      height: 42px;
      display: grid;
      place-items: center;
      border-radius: 10px;
      background: #f1f5f9;
      font-size: 20px;
    }

    .expense-name {
      font-weight: 600;
    }

    .expense-date {
      font-size: 12px;
      color: #94a3b8;
      margin-top: 3px;
    }

    .expense-price {
      color: #dc2626;
      font-weight: 700;
    }

    /* SAVING */
    .saving-box {
      background: linear-gradient(135deg, #16a34a, #22c55e);
      color: white;
      padding: 25px;
      border-radius: 16px;
    }

    .saving-box h3 {
      margin-bottom: 12px;
    }

    .saving-amount {
      font-size: 32px;
      font-weight: 800;
      margin-bottom: 15px;
    }

    .saving-progress {
      background: rgba(255,255,255,.25);
      height: 9px;
      border-radius: 20px;
      overflow: hidden;
    }

    .saving-progress div {
      width: 68%;
      height: 100%;
      background: white;
    }

    /* MODAL */
    .modal {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15,23,42,.55);
      align-items: center;
      justify-content: center;
      z-index: 10;
    }

    .modal.show {
      display: flex;
    }

    .modal-box {
      background: white;
      width: 400px;
      padding: 30px;
      border-radius: 18px;
    }

    .modal-box h2 {
      margin-bottom: 20px;
    }

    .input-group {
      margin-bottom: 15px;
    }

    .input-group label {
      display: block;
      font-size: 14px;
      margin-bottom: 6px;
    }

    .input-group input,
    .input-group select {
      width: 100%;
      padding: 12px;
      border: 1px solid #dbe1e8;
      border-radius: 9px;
      outline: none;
    }

    .modal-actions {
      display: flex;
      gap: 10px;
      margin-top: 20px;
    }

    .cancel {
      background: #e5e7eb;
      color: #334155;
    }

    /* MOBILE */
    @media (max-width: 900px) {
      .sidebar {
        width: 70px;
        padding: 20px 8px;
      }

      .logo {
        font-size: 0;
      }

      .logo span {
        font-size: 22px;
      }

      .menu a span:last-child {
        display: none;
      }

      .main {
        margin-left: 70px;
        width: calc(100% - 70px);
        padding: 20px;
      }

      .cards {
        grid-template-columns: repeat(2, 1fr);
      }

      .grid {
        grid-template-columns: 1fr;
      }
    }

    @media (max-width: 600px) {
      .cards {
        grid-template-columns: 1fr;
      }

      .topbar {
        align-items: flex-start;
        gap: 15px;
        flex-direction: column;
      }
    }
  </style>
</head>

<body>

<div class="app">

  <!-- SIDEBAR -->
  <aside class="sidebar">
    <div class="logo">
      Money<span>Plan</span>
    </div>

    <ul class="menu">
      <li>
        <a href="#" class="active">
          <span>📊</span>
          <span>ภาพรวม</span>
        </a>
      </li>

      <li>
        <a href="#">
          <span>💰</span>
          <span>รายรับ</span>
        </a>
      </li>

      <li>
        <a href="#">
          <span>💸</span>
          <span>รายจ่าย</span>
        </a>
      </li>

      <li>
        <a href="#">
          <span>🎯</span>
          <span>เป้าหมาย</span>
        </a>
      </li>

      <li>
        <a href="#">
          <span>⚙️</span>
          <span>ตั้งค่า</span>
        </a>
      </li>
    </ul>
  </aside>


  <!-- MAIN -->
  <main class="main">

    <div class="topbar">
      <div>
        <h1>สวัสดี 👋</h1>
        <p style="color:#64748b;margin-top:5px;">
          มาดูแผนการเงินของคุณกัน
        </p>
      </div>

      <select class="month">
        <option>สิงหาคม 2026</option>
        <option>กรกฎาคม 2026</option>
        <option>มิถุนายน 2026</option>
      </select>
    </div>


    <!-- SUMMARY -->
    <section class="cards">

      <div class="card">
        <div class="label">รายรับทั้งหมด</div>
        <div class="value green">฿35,000</div>
      </div>

      <div class="card">
        <div class="label">รายจ่าย</div>
        <div class="value red">฿18,450</div>
      </div>

      <div class="card">
        <div class="label">เงินออม</div>
        <div class="value blue">฿8,000</div>
      </div>

      <div class="card">
        <div class="label">เงินคงเหลือ</div>
        <div class="value purple">฿8,550</div>
      </div>

    </section>


    <div class="grid">

      <!-- LEFT -->
      <div>

        <!-- BUDGET -->
        <div class="panel">

          <div class="panel-header">
            <h2>📌 งบประมาณเดือนนี้</h2>
            <button class="btn" onclick="openModal()">
              + เพิ่มรายการ
            </button>
          </div>

          <div class="budget-item">
            <div class="budget-top">
              <span class="budget-name">🍜 อาหาร</span>
              <span class="budget-money">฿3,600 / ฿5,000</span>
            </div>
            <div class="progress">
              <div class="progress-bar food"></div>
            </div>
          </div>

          <div class="budget-item">
            <div class="budget-top">
              <span class="budget-name">🏠 ค่าใช้จ่ายบ้าน</span>
              <span class="budget-money">฿4,500 / ฿10,000</span>
            </div>
            <div class="progress">
              <div class="progress-bar home"></div>
            </div>
          </div>

          <div class="budget-item">
            <div class="budget-top">
              <span class="budget-name">🚗 เดินทาง</span>
              <span class="budget-money">฿900 / ฿3,000</span>
            </div>
            <div class="progress">
              <div class="progress-bar travel"></div>
            </div>
          </div>

          <div class="budget-item">
            <div class="budget-top">
              <span class="budget-name">🛍️ ช้อปปิ้ง</span>
              <span class="budget-money">฿1,800 / ฿3,000</span>
            </div>
            <div class="progress">
              <div class="progress-bar shopping"></div>
            </div>
          </div>

        </div>


        <!-- EXPENSE -->
        <div class="panel">

          <div class="panel-header">
            <h2>🧾 รายจ่ายล่าสุด</h2>
            <button class="btn" onclick="openModal()">+ เพิ่ม</button>
          </div>

          <div id="expenseList">

            <div class="expense">
              <div class="expense-left">
                <div class="icon">🍜</div>
                <div>
                  <div class="expense-name">อาหารกลางวัน</div>
                  <div class="expense-date">17 ส.ค. 2026</div>
                </div>
              </div>
              <div class="expense-price">- ฿120</div>
            </div>

            <div class="expense">
              <div class="expense-left">
                <div class="icon">🚕</div>
                <div>
                  <div class="expense-name">ค่าเดินทาง</div>
                  <div class="expense-date">16 ส.ค. 2026</div>
                </div>
              </div>
              <div class="expense-price">- ฿180</div>
            </div>

            <div class="expense">
              <div class="expense-left">
                <div class="icon">🛒</div>
                <div>
                  <div class="expense-name">ซื้อของใช้</div>
                  <div class="expense-date">15 ส.ค. 2026</div>
                </div>
              </div>
              <div class="expense-price">- ฿560</div>
            </div>

          </div>

        </div>

      </div>


      <!-- RIGHT -->
      <div>

        <div class="saving-box">

          <h3>🎯 เป้าหมายเงินออม</h3>

          <div class="saving-amount">
            ฿8,000
          </div>

          <p style="margin-bottom:12px;">
            เป้าหมาย ฿12,000
          </p>

          <div class="saving-progress">
            <div></div>
          </div>

          <p style="margin-top:12px;font-size:14px;">
            ทำได้แล้ว 68%
          </p>

        </div>


        <div class="panel" style="margin-top:20px;">

          <div class="panel-header">
            <h2>💡 คำแนะนำ</h2>
          </div>

          <p style="line-height:1.8;color:#64748b;">
            เดือนนี้คุณใช้จ่ายด้านอาหารไปแล้ว
            <strong style="color:#f97316;">72%</strong>
            ของงบประมาณ
            <br><br>
            ลองลดค่าอาหารนอกบ้านอีกเล็กน้อย
            เพื่อให้มีเงินเหลือสำหรับเงินออมมากขึ้น
          </p>

        </div>

      </div>

    </div>

  </main>
</div>


<!-- MODAL -->
<div class="modal" id="modal">

  <div class="modal-box">

    <h2>เพิ่มรายจ่าย</h2>

    <div class="input-group">
      <label>ชื่อรายการ</label>
      <input type="text" id="expenseName"
             placeholder="เช่น ค่าอาหาร">
    </div>

    <div class="input-group">
      <label>จำนวนเงิน</label>
      <input type="number" id="expenseAmount"
             placeholder="0">
    </div>

    <div class="input-group">
      <label>หมวดหมู่</label>
      <select>
        <option>อาหาร</option>
        <option>เดินทาง</option>
        <option>บ้าน</option>
        <option>ช้อปปิ้ง</option>
        <option>อื่นๆ</option>
      </select>
    </div>

    <div class="modal-actions">

      <button class="btn" onclick="addExpense()">
        บันทึก
      </button>

      <button class="btn cancel" onclick="closeModal()">
        ยกเลิก
      </button>

    </div>

  </div>

</div>


<script>

  function openModal() {
    document.getElementById("modal").classList.add("show");
  }

  function closeModal() {
    document.getElementById("modal").classList.remove("show");
  }

  function addExpense() {

    const name =
      document.getElementById("expenseName").value;

    const amount =
      document.getElementById("expenseAmount").value;

    if (!name || !amount) {
      alert("กรุณากรอกข้อมูลให้ครบ");
      return;
    }

    const list =
      document.getElementById("expenseList");

    const item = document.createElement("div");

    item.className = "expense";

    item.innerHTML = `
      <div class="expense-left">
        <div class="icon">💸</div>
        <div>
          <div class="expense-name">${name}</div>
          <div class="expense-date">วันนี้</div>
        </div>
      </div>

      <div class="expense-price">
        - ฿${Number(amount).toLocaleString()}
      </div>
    `;

    list.prepend(item);

    document.getElementById("expenseName").value = "";
    document.getElementById("expenseAmount").value = "";

    closeModal();
  }

</script>

</body>
</html>