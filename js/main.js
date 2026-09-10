// ===================================================================
// しまたび沖縄 共通スクリプト
// ===================================================================

document.addEventListener("DOMContentLoaded", () => {
  // モバイルナビ開閉
  const toggle = document.querySelector(".nav-toggle");
  const nav = document.querySelector(".main-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", () => nav.classList.toggle("open"));
    nav.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => nav.classList.remove("open"))
    );
  }

  // カテゴリ / エリア絞り込みタブ（spots.html, restaurants.html）
  const tabGroups = document.querySelectorAll("[data-filter-group]");
  tabGroups.forEach((group) => {
    const buttons = group.querySelectorAll("button[data-filter]");
    const targetSelector = group.dataset.filterGroup;
    const items = document.querySelectorAll(targetSelector);

    buttons.forEach((btn) => {
      btn.addEventListener("click", () => {
        buttons.forEach((b) => b.classList.remove("active"));
        btn.classList.add("active");
        const value = btn.dataset.filter;

        items.forEach((item) => {
          const match = value === "all" || item.dataset.category === value || item.dataset.area === value;
          item.style.display = match ? "" : "none";
        });

        // エリア見出しごと非表示にする（該当カードが1件も無い場合）
        document.querySelectorAll("[data-area-section]").forEach((sec) => {
          const visible = sec.querySelectorAll(targetSelector + ':not([style*="display: none"])');
          sec.style.display = visible.length > 0 ? "" : "none";
        });
      });
    });
  });

  // 航空券検索リンク生成（flights.html）
  const flightForm = document.getElementById("flight-search-form");
  if (flightForm) {
    flightForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const origin = document.getElementById("origin-select").value;
      const dest = "OKA"; // 那覇空港固定
      // Skyscanner のディープリンク（アフィリエイトID不要で検索結果に遷移できる形式）
      const url = `https://www.skyscanner.jp/transport/flights/${origin.toLowerCase()}/${dest.toLowerCase()}/`;
      window.open(url, "_blank", "noopener");
    });
  }
});
