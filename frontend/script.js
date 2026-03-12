class SkinAnalyzer {
    constructor() {
        this.API_URL = 'http://localhost:8000/predict';
        this.init();
    }

    init() {
        this.uploadZone = document.getElementById('uploadZone');
        this.imageInput = document.getElementById('imageInput');
        this.previewImg = document.getElementById('previewImg');
        this.preview = document.getElementById('preview');
        this.predictBtn = document.getElementById('predictBtn');
        this.uploadSection = document.getElementById('upload-section');
        this.loading = document.getElementById('loading');
        this.results = document.getElementById('results');
        this.analyzeAgain = document.getElementById('analyzeAgain');

        // Drag & drop
        this.uploadZone.addEventListener('click', () => this.imageInput.click());
        this.imageInput.addEventListener('change', (e) => this.handleImageSelect(e));
        
        ['dragover', 'dragenter'].forEach(event => {
            this.uploadZone.addEventListener(event, (e) => this.handleDragState(e), false);
        });
        
        ['dragleave', 'drop'].forEach(event => {
            this.uploadZone.addEventListener(event, (e) => this.handleDragState(e), false);
        });
        this.uploadZone.addEventListener('drop', (e) => this.handleImageDrop(e), false);

        this.predictBtn.addEventListener('click', () => this.predict());
        this.analyzeAgain.addEventListener('click', () => this.reset());

        // Prevent form submit
        document.addEventListener('dragover', this.preventDefaults, false);
    }

    preventDefaults(e) {
        e.preventDefault();
        e.stopPropagation();
    }

    handleDragState(e) {
        this.preventDefaults(e);
        this.uploadZone.classList.toggle(
            'dragging',
            e.type === 'dragover' || e.type === 'dragenter'
        );
    }

    handleImageSelect(e) {
        const file = e.target.files[0];
        if (file && this.isValidImage(file)) {
            this.showPreview(file);
        }
    }

    handleImageDrop(e) {
        this.handleDragState(e);
        const file = e.dataTransfer.files[0];
        if (file && this.isValidImage(file)) {
            this.imageInput.files = e.dataTransfer.files;
            this.showPreview(file);
        }
    }

    isValidImage(file) {
        const validTypes = ['image/jpeg', 'image/png', 'image/jpg'];
        const maxSize = 10 * 1024 * 1024; // 10MB
        if (!validTypes.includes(file.type)) {
            alert('Please upload JPG or PNG images only.');
            return false;
        }
        if (file.size > maxSize) {
            alert('Image too large. Max 10MB.');
            return false;
        }
        return true;
    }

    showPreview(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            this.previewImg.src = e.target.result;
            this.uploadZone.classList.add('hidden');
            this.preview.classList.remove('hidden');
        };
        reader.readAsDataURL(file);
    }

    async predict() {
        this.predictBtn.disabled = true;
        this.predictBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Analyzing...';
        
        this.uploadSection.classList.add('hidden');
        this.loading.classList.remove('hidden');

        try {
            const formData = new FormData();
            formData.append('file', this.imageInput.files[0]);

            const response = await fetch(this.API_URL, {
                method: 'POST',
                body: formData
            });

            if (!response.ok) {
                const errorBody = await response.json().catch(() => null);
                const errorMessage = errorBody?.detail || `API Error: ${response.status}`;
                throw new Error(errorMessage);
            }

            const result = await response.json();
            this.displayResults(result);
        } catch (error) {
            console.error('Prediction error:', error);
            alert('Analysis failed. Make sure backend is running on localhost:8000. ' + error.message);
            this.reset();
        }
    }

    displayResults(result) {
        document.getElementById('disease').textContent = result.disease;
        
        const severityEl = document.getElementById('severity');
        severityEl.textContent = result.severity;
        severityEl.className = `severity-badge ${this.getSeverityClass(result.severity)}`;
        
        const confPercent = (result.confidence * 100).toFixed(1);
        document.getElementById('confidenceFill').style.width = `${confPercent}%`;
        document.getElementById('confidenceText').textContent = `${confPercent}%`;

        this.loading.classList.add('hidden');
        this.results.classList.remove('hidden');
    }

    getSeverityClass(severity) {
        const severityMap = {
            'Early Stage': 'severity-early',
            'Moderate Stage': 'severity-mild',
            'Severe Stage': 'severity-severe'
        };
        return severityMap[severity] || 'severity-mild';
    }

    reset() {
        this.imageInput.value = '';
        this.uploadZone.classList.remove('hidden');
        this.uploadZone.classList.remove('dragging');
        this.preview.classList.add('hidden');
        this.loading.classList.add('hidden');
        this.results.classList.add('hidden');
        this.predictBtn.disabled = false;
        this.predictBtn.innerHTML = '<i class="fas fa-brain"></i> Analyze Skin';
    }
}

new SkinAnalyzer();
